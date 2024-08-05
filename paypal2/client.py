import base64
import json
import ssl
import zlib
from contextlib import asynccontextmanager
from datetime import datetime, timezone, timedelta
from typing import Any
from typing import Optional, Literal

import aiohttp
import certifi
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from aiohttp import TCPConnector
from pydantic import BaseModel
from ttldict2 import TTLDict

from paypal2.models.order import OrderMinimalResponse
from paypal2.models.order import OrdersCreate
from paypal2.models.payment import CapturedPayment
from paypal2.models.plan import PlanCreate, PlanDetails, PlanList, PlanMinimalResponse
from paypal2.models.product import ProductDetails, ProductCreate, ProductList
from paypal2.models.subscription import (
    SubscriptionMinimalResponse,
    SubscriptionCreate,
    SubscriptionDetails,
    SubscriptionReason,
    SubscriptionTransactionList,
)


class AccessTokenReset(Exception):
    pass


class JsonBadRequest(aiohttp.ClientResponseError):
    @classmethod
    def from_cre(cls, cre: aiohttp.ClientResponseError, data: Any):
        return cls(
            cre.request_info,
            cre.history,
            code=cre.code,
            status=cre.status,
            message=cre.message,
            headers=cre.headers,
            data=data,
        )

    def __init__(self, request_info, history, *, code=None, status=None, message="", headers=None, data=None) -> None:
        aiohttp.ClientResponseError.__init__(
            self, request_info, history, code=code, status=status, message=message, headers=headers
        )
        self.data = data


class AbstractExternalWebHookCertificateStore:
    async def get(self, url: str) -> Optional[bytes]:
        raise NotImplementedError()

    async def set(self, url: str, content: bytes):
        raise NotImplementedError()


class PayPalApiClient:
    __slots__ = (
        "client_id",
        "__client_secret",
        "url_base",
        "proxy_address",
        "session",
        "session_owned",
        "webhook_id",
        "external_cert_store",
        "_access_token",
        "_cert_cache",
    )

    PRODUCTION_URL_BASE = "https://api-m.paypal.com"
    SANDBOX_URL_BASE = "https://api-m.sandbox.paypal.com"

    @classmethod
    def init_session(cls):
        return aiohttp.ClientSession(
            connector=TCPConnector(ssl=ssl.create_default_context(cafile=certifi.where()), limit=16)
        )

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        url_base: str = None,
        proxy_address: str = None,
        session: aiohttp.ClientSession = None,
        webhook_id: str = None,
        external_cert_store: Optional[AbstractExternalWebHookCertificateStore] = None,
    ):
        self.client_id = client_id
        self.__client_secret = client_secret
        self.url_base = (url_base or self.PRODUCTION_URL_BASE).rstrip("/")
        self.proxy_address = proxy_address
        self.session_owned = session is None
        self.session = session
        self.webhook_id = webhook_id
        self.external_cert_store = external_cert_store
        # state
        self._access_token = None
        self._cert_cache = TTLDict(14 * 24 * 60 * 60.0, max_items=10)

    async def setup(self, session: aiohttp.ClientSession = None):
        if self.session is None:
            self.session_owned = session is None
            if self.session_owned:
                session = self.init_session()
            self.session = session

    async def close(self):
        if self.session is not None:
            if self.session_owned:
                await self.session.close()
            self.session = None

    async def _get_access_token(self):
        token = base64.b64encode(f"{self.client_id}:{self.__client_secret}".encode()).decode()
        async with self.session.post(
            self.url_base + "/v1/oauth2/token",
            data="grant_type=client_credentials",
            headers={"Content-Type": "application/x-www-form-urlencoded", "Authorization": f"Basic {token}"},
            proxy=self.proxy_address,
        ) as resp:
            resp.raise_for_status()
            data = await resp.json()
        access_token = data.get("access_token")
        if not isinstance(access_token, str):
            raise Exception("PayPal auth error")
        return access_token

    @asynccontextmanager
    async def _manage_access_token(self, raise_reset: bool = False):
        if not self._access_token:
            self._access_token = await self._get_access_token()
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
        params: Optional[dict[str, str]] = None,
        retry: int = 2,
        response_body: bool = True,
    ):
        j = body.model_dump(mode="json", exclude_unset=True) if isinstance(body, BaseModel) else body
        for i in range(1, retry + 1):
            try:
                async with self._manage_access_token(raise_reset=i < retry) as access_token:
                    hs = {"Authorization": f"Bearer {access_token}"}
                    if headers:
                        hs.update(headers)
                    async with getattr(self.session, method)(
                        self.url_base + url, json=j, headers=hs, params=params, proxy=self.proxy_address
                    ) as resp:
                        try:
                            resp.raise_for_status()
                        except aiohttp.ClientResponseError as e:
                            if e.status == 400:
                                try:
                                    details = await resp.json()
                                except Exception:
                                    raise e
                                else:
                                    raise JsonBadRequest.from_cre(e, details)
                            raise e
                        if response_body:
                            return await resp.json()
            except AccessTokenReset:
                pass

    async def order_create(self, request: OrdersCreate) -> OrderMinimalResponse:
        """
        Create an order for purchase approval.
        """
        data = await self._retry_request("post", "/v2/checkout/orders", request)
        return OrderMinimalResponse.model_validate(data)

    async def order_capture(self, order_id: str) -> OrderMinimalResponse:
        """
        :param order_id: Must be checked that this service created the order previously, and knows how to handle the
            capture if it is completed.
        :return: the status property indicates success if "COMPLETED"
        """
        data = await self._retry_request(
            "post", f"/v2/checkout/orders/{order_id}/capture", {}, {"Prefer": "return=minimal"}
        )
        return OrderMinimalResponse.model_validate(data)

    async def subscription_create(self, request: SubscriptionCreate) -> SubscriptionMinimalResponse:
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

    async def subscription_transaction_list(
        self, subscription_id: str, start_time: datetime = None, end_time: datetime = None
    ) -> Optional[SubscriptionTransactionList]:
        if not start_time:
            start_time = datetime.utcnow() - timedelta(minutes=60)
        if not end_time:
            end_time = datetime.utcnow() + timedelta(minutes=10)
        try:
            data = await self._retry_request(
                "get",
                f"/v1/billing/subscriptions/{subscription_id}/transactions",
                params={
                    "start_time": start_time.replace(tzinfo=timezone.utc).isoformat(timespec="seconds"),
                    "end_time": end_time.replace(tzinfo=timezone.utc).isoformat(timespec="seconds"),
                },
            )
        except aiohttp.ClientResponseError as e:
            if e.status == 404:
                return None
            raise e
        return SubscriptionTransactionList.model_validate(data)

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

    async def plan_create(self, request: PlanCreate) -> PlanMinimalResponse:
        data = await self._retry_request("post", "/v1/billing/plans", request)
        return PlanMinimalResponse.model_validate(data)

    async def plan_list(self) -> PlanList:
        data = await self._retry_request("get", "/v1/billing/plans")
        return PlanList.model_validate(data)

    async def plan_details(self, plan_id: str) -> Optional[PlanDetails]:
        try:
            data = await self._retry_request("get", f"/v1/billing/plans/{plan_id}")
        except aiohttp.ClientResponseError as e:
            if e.status == 404:
                return None
            raise e
        return PlanDetails.model_validate(data)

    # async def plan_update(self, plan_id: str, ops: list[PlanUpdate]):
    #     await self._retry_request("patch", f"/v1/billings/plans/{plan_id}", ops, response_body=False)

    async def captured_payment_details(self, capture_id: str) -> Optional[CapturedPayment]:
        try:
            data = await self._retry_request("get", f"/v2/payments/captures/{capture_id}")
        except aiohttp.ClientResponseError as e:
            if e.status == 404:
                return None
            raise e
        return CapturedPayment.model_validate(data)

    async def verify_webhook_notification(self, body: bytes, headers: dict[str, str], webhook_id: str = None) -> dict:
        """
        WebHook notification verification.
        """
        webhook_id = webhook_id or self.webhook_id
        if not isinstance(webhook_id, str):
            raise ValueError("Paypal webhook id not configured")
        transmission_auth_algo = headers.get("paypal-auth-algo", "SHA256withRSA")  # default
        if transmission_auth_algo != "SHA256withRSA":
            raise ValueError(f"Paypal webhook signature algorithm not supported: {transmission_auth_algo}")
        transmission_signature = headers.get("paypal-transmission-sig")
        transmission_id = headers.get("paypal-transmission-id")
        transmission_time = headers.get("paypal-transmission-time")
        transmission_cert_url = headers.get("paypal-cert-url")
        if (
            not isinstance(transmission_signature, str)
            or not isinstance(transmission_id, str)
            or not isinstance(transmission_time, str)
            or not isinstance(transmission_cert_url, str)
        ):
            raise ValueError("Paypal webhook headers invalid")
        if self.url_base != self.SANDBOX_URL_BASE and not transmission_cert_url.startswith("https://api.paypal.com/"):
            raise ValueError("Paypal webhook cert url is not from PayPal API")
        rsa_pub_key = self._cert_cache.get(transmission_cert_url, touch=True)
        if not rsa_pub_key:
            transmission_cert = None
            if self.external_cert_store:
                transmission_cert = await self.external_cert_store.get(transmission_cert_url)
            if not transmission_cert:
                async with self.session.get(transmission_cert_url) as r:
                    r.raise_for_status()
                    transmission_cert = await r.read()
            rsa_pub_key = RSA.import_key(transmission_cert)
            if rsa_pub_key.has_private():
                raise ValueError("Paypal webhook transmission key imported as private")
            if self.external_cert_store:
                await self.external_cert_store.set(transmission_cert_url, transmission_cert)
            self._cert_cache[transmission_cert_url] = rsa_pub_key
        # TODO: crc, hash, signature check and json load could be offloaded to worker thread?
        body_checksum = zlib.crc32(body)
        message = f"{transmission_id}|{transmission_time}|{webhook_id}|{body_checksum}"
        hashed = SHA256.new(message.encode())
        pkcs1_15.new(rsa_pub_key).verify(hashed, base64.b64decode(transmission_signature))
        data = json.loads(body)
        if not isinstance(data, dict):
            raise ValueError("Paypal webhook data is not dict")
        return data
