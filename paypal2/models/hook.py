from typing import Optional, ClassVar

from pydantic import BaseModel, Field

from paypal2.models.common import HATEOASLink


class WebHookEvent(BaseModel):
    HANDLER_KEY: ClassVar[Optional[tuple[str, str, str]]] = None
    id: str
    event_type: str
    event_version: str
    resource_type: str
    resource_version: Optional[str] = None
    resource: dict
    links: list[HATEOASLink]


class WebHookSubscriptionResourceV2(BaseModel):
    id: str
    status: str
    plan_id: str
    links: list[HATEOASLink]


class MonetaryTotal(BaseModel):
    currency: str = Field(min_length=3, max_length=3)
    total: str = Field(max_length=32)


class WebHookSaleResource(BaseModel):
    id: str
    state: str
    amount: Optional[MonetaryTotal] = None
    links: list[HATEOASLink]
    # todo custom_id here maybe?


class WebHookEventSubscriptionCreated(WebHookEvent):
    HANDLER_KEY: ClassVar = ("BILLING.SUBSCRIPTION.CREATED", "subscription", "2.0")
    resource: WebHookSubscriptionResourceV2


class WebHookEventSaleCompleted(WebHookEvent):
    HANDLER_KEY: ClassVar = ("PAYMENT.SALE.COMPLETED", "sale", "1.0")
    resource: WebHookSaleResource
