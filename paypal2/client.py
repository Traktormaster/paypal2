import base64
import ssl
from contextlib import asynccontextmanager
from typing import Optional, Literal

import aiohttp
import certifi
from aiohttp import TCPConnector
from pydantic import BaseModel

from paypal2.models.order import OrdersCreate, OrderMinimalResponse
from paypal2.models.plan import PlanCreate, PlanDetails
from paypal2.models.product import ProductDetails, ProductCreate, ProductList
from paypal2.models.subscription import (
    SubscriptionMinimalResponse,
    SubscriptionCreate,
    SubscriptionDetails,
    SubscriptionReason,
)


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
    async def _access_token(self, raise_reset: bool = False):
        if not self._access_token:
            self._access_token = await self._access_token()
        access_token = self._access_token
        try:
            yield access_token
        except aiohttp.ClientResponseError as e:
            if e.status == 401:
                if self._access_token == access_token:
                    self._access_token = None
                if raise_reset:
                    raise AccessTokenReset() from e
            raise e

    async def _retry_request(
        self,
        method: Literal["get"] | Literal["post"] | Literal["patch"],
        url: str,
        body: BaseModel | dict | list | None = None,
        headers: dict[str, str] = None,
        retry: int = 2,
        response_body: bool = True,
    ):
        j = body.model_dump(exclude_unset=True) if isinstance(body, BaseModel) else body
        for i in range(1, retry + 1):
            try:
                async with self._access_token(raise_reset=i < retry) as access_token:
                    hs = {"Authorization": f"Bearer {access_token}"}
                    if headers:
                        hs.update(headers)
                    async with getattr(self.session, method)(
                        self.url_base + url, json=j, headers=hs, proxy=self.proxy_address
                    ) as resp:
                        resp.raise_for_status()
                        if response_body:
                            return await resp.json()
            except AccessTokenReset:
                pass

    async def create_order(self, request: OrdersCreate) -> OrderMinimalResponse:
        """
        Create an order for purchase approval.
        """
        data = await self._retry_request("post", "/v2/checkout/orders", request)
        return OrderMinimalResponse.model_validate(data)

    async def capture_order(self, order_id: str) -> OrderMinimalResponse:
        """
        :param order_id: Must be checked that this service created the order previously, and knows how to handle the
            capture if it is completed.
        :return: the status property indicates success if "COMPLETED"
        """
        data = await self._retry_request(
            "post", f"/v2/checkout/orders/{order_id}/capture", {}, {"Prefer": "return=minimal"}
        )
        return OrderMinimalResponse.model_validate(data)

    async def create_subscription(self, request: SubscriptionCreate) -> SubscriptionMinimalResponse:
        """
        Create a subscription for client approval.
        """
        data = await self._retry_request("post", "/v1/billing/subscriptions", request)
        return SubscriptionMinimalResponse.model_validate(data)

    async def subscription_details(self, subscription_id: str) -> Optional[SubscriptionDetails]:
        try:
            data = await self._retry_request("get", f"/v1/billing/subscriptions/{subscription_id}")
        except aiohttp.ClientResponseError as e:
            if e.status == 404:
                return None
            raise e
        return SubscriptionDetails.model_validate(data)

    async def subscription_activate(self, subscription_id: str, request: SubscriptionReason):
        await self._retry_request(
            "post", f"/v1/billing/subscriptions/{subscription_id}/activate", request, response_body=False
        )

    async def subscription_suspend(self, subscription_id: str, request: SubscriptionReason):
        await self._retry_request(
            "post", f"/v1/billing/subscriptions/{subscription_id}/suspend", request, response_body=False
        )

    async def subscription_cancel(self, subscription_id: str, request: SubscriptionReason):
        await self._retry_request(
            "post", f"/v1/billing/subscriptions/{subscription_id}/cancel", request, response_body=False
        )

    async def product_create(self, request: ProductCreate) -> ProductDetails:
        data = await self._retry_request("post", "/v1/catalogs/products", request, {"Prefer": "return=representation"})
        return ProductDetails.model_validate(data)

    async def product_list(self) -> ProductList:
        data = await self._retry_request("get", "/v1/catalogs/products")
        return ProductList.model_validate(data)

    async def product_details(self, product_id: str) -> Optional[ProductDetails]:
        try:
            data = await self._retry_request("get", f"/v1/catalogs/products/{product_id}")
        except aiohttp.ClientResponseError as e:
            if e.status == 404:
                return None
            raise e
        return ProductDetails.model_validate(data)

    async def create_plan(self, request: PlanCreate):
        data = await self._retry_request("post", "/v2/billing/plans", request)
        if not isinstance(data, dict):
            raise ValueError("PayPal api response not dict")
        if not isinstance(data.get("id"), str):
            raise ValueError("PayPal create-order api response has no valid id")
        return data

    async def plan_details(self, plan_id: str) -> Optional[PlanDetails]:
        try:
            data = await self._retry_request("get", f"/v1/billings/plans/{plan_id}")
        except aiohttp.ClientResponseError as e:
            if e.status == 404:
                return None
            raise e
        return PlanDetails.model_validate(data)

    # async def plan_update(self, plan_id: str, ops: list[PlanUpdate]):
    #     await self._retry_request("patch", f"/v1/billings/plans/{plan_id}", ops, response_body=False)
