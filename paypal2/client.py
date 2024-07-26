import base64
import ssl
from contextlib import asynccontextmanager
from typing import Optional, Literal

import aiohttp
import certifi
from aiohttp import TCPConnector
from pydantic import BaseModel, Field


class MonetaryValue(BaseModel):
    currency_code: str = Field(min_length=3, max_length=3)
    value: str = Field(max_length=32)


class Breakdown(BaseModel):
    item_total: Optional[MonetaryValue]
    shipping: Optional[MonetaryValue]
    handling: Optional[MonetaryValue]
    tax_total: Optional[MonetaryValue]
    insurance: Optional[MonetaryValue]
    shipping_discount: Optional[MonetaryValue]
    discount: Optional[MonetaryValue]


class MonetaryValueWithBreakdown(MonetaryValue):
    breakdown: Optional[Breakdown]


class Item(BaseModel):
    name: str = Field(min_length=1, max_length=127)
    quantity: str = Field(min_length=1, max_length=10)
    description: Optional[str] = Field(min_length=1, max_length=127)
    sku: Optional[str] = Field(min_length=1, max_length=127)
    url: Optional[str] = Field(min_length=1, max_length=2048)
    category: Optional[Literal["DIGITAL_GOODS", "PHYSICAL_GOODS", "DONATION"]] = Field(min_length=1, max_length=20)
    image_url: Optional[str] = Field(
        min_length=1, max_length=2048, pattern=r"^(https:)([/|.|\w|\s|-])*\.(?:jpg|gif|png|jpeg|JPG|GIF|PNG|JPEG)"
    )
    unit_amount: MonetaryValue  # purchase_units[].amount.breakdown.item_total must be set if present
    tax: Optional[MonetaryValue]  # purchase_units[].amount.breakdown.tax_total must be set if present
    # TODO: upc


class PurchaseUnit(BaseModel):
    reference_id: Optional[str] = Field(min_length=1, max_length=256)
    description: Optional[str] = Field(min_length=1, max_length=127)
    custom_id: Optional[str] = Field(min_length=1, max_length=256)
    invoice_id: Optional[str] = Field(min_length=1, max_length=256)
    soft_descriptor: Optional[str] = Field(min_length=1, max_length=22)
    items: Optional[list[Item]]


class OrdersCreate(BaseModel):
    purchase_units: list[PurchaseUnit] = Field(min_length=1, max_length=10)
    category: Optional[Literal["CAPTURE", "AUTHORIZE"]]
    # TODO: payment_source


class AccessTokenReset(Exception):
    pass


class PayPalApiClient:
    __slots__ = (
        "_client_id",
        "__client_secret",
        "session",
        "session_owned",
        "proxy_address",
        "url_base",
        "_access_token",
    )

    PRODUCTION_URL_BASE = "https://api-m.paypal.com"
    SANDBOX_URL_BASE = "https://api-m.sandbox.paypal.com"

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        session: aiohttp.ClientSession = None,
        url_base: str = PRODUCTION_URL_BASE,
        proxy_address: str = None,
    ):
        self._client_id = client_id
        self.__client_secret = client_secret
        self.session_owned = session is None
        self.session = session
        self.url_base = url_base
        self.proxy_address = proxy_address
        # state
        self._access_token = None

    async def setup(self, session: aiohttp.ClientSession = None):
        if self.session is None:
            self.session_owned = session is None
            if self.session_owned:
                session = aiohttp.ClientSession(
                    connector=TCPConnector(ssl=ssl.create_default_context(cafile=certifi.where()), limit=16)
                )
            self.session = session

    async def close(self):
        if self.session is not None:
            if self.session_owned:
                await self.session.close()
            self.session = None

    async def _get_access_token(self):
        token = base64.b64encode(f"{self._client_id}:{self.__client_secret}".encode()).decode()
        async with self.session.post(
            self.url_base + "/v1/oauth2/token",
            data="grant_type=client_credentials",
            headers={"Authorization": f"Bearer {token}"},
            proxy=self.proxy_address,
        ) as resp:
            resp.raise_for_status()
            data = await resp.json()
        access_token = data.get("access_token")
        if not isinstance(access_token, str):
            raise Exception("PayPal auth error")
        return access_token

    @asynccontextmanager
    async def _access_token(self):
        if not self._access_token:
            self._access_token = await self._access_token()
        access_token = self._access_token
        try:
            yield access_token
        except aiohttp.ClientResponseError as e:
            if e.status == 401:
                if self._access_token == access_token:
                    self._access_token = None
                    raise AccessTokenReset() from e
            raise e

    async def _retry_post(self, url: str, body: BaseModel | dict, headers: dict[str, str] = None):
        j = body.model_dump(exclude_unset=True) if isinstance(body, BaseModel) else body
        for i in range(2):
            try:
                async with self._access_token() as access_token:

                    hs = {"Authorization": f"Bearer {access_token}"}
                    if headers:
                        hs.update(headers)
                    async with self.session.post(
                        self.url_base + url, json=j, headers=hs, proxy=self.proxy_address
                    ) as resp:
                        resp.raise_for_status()
                        return await resp.json()
            except AccessTokenReset:
                if i != 0:
                    raise

    async def create_order(self, request: OrdersCreate):
        data = await self._retry_post("/v2/checkout/orders", request)
        # TODO: validate data
        data.get("id")  # record order id for account
        data.get("links")  # return approve link to client

    async def capture_order(self, order_id: str):
        data = await self._retry_post(f"/v2/checkout/orders/{order_id}/capture", {}, {"Prefer": "return=minimal"})
        # TODO: validate data
        data.get("status") == "COMPLETED"
