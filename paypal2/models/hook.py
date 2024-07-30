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
    status_update_time: Optional[str] = None
    plan_id: str
    start_time: Optional[str] = None
    auto_renewal: Optional[bool] = None
    links: list[HATEOASLink]
    # todo quantity
    # todo shipping_amount
    # todo subscriber
    # todo billing_info
    # todo create_time
    # todo update_time


class WebHookPlanResourceV2(BaseModel):
    id: str
    product_id: str
    status: str
    name: Optional[str] = None
    description: Optional[str] = None
    usage_type: Optional[str] = None
    links: list[HATEOASLink]
    # todo billing_cycles
    # todo payment_preferences
    # todo taxes
    # todo create_time
    # todo update_time


class MonetaryTotal(BaseModel):
    currency: str = Field(max_length=5)
    total: str = Field(max_length=50)
    details: Optional[dict] = None


class WebHookSaleResource(BaseModel):
    id: str
    state: str
    amount: Optional[MonetaryTotal] = None
    links: list[HATEOASLink]
    # todo create_time
    # todo update_time for complete, refund
    # todo sale_id for refund
    # todo parent_payment for complete, refund
    # todo clearing_time for complete
    # todo payment_mode for complete
    # todo protection_eligibility for complete
    # todo protection_eligibility_type for complete

    # fixme is custom_id here if it is set on subscription maybe? (if not it can be queried by the payments/details)


class WebHookEventSubscriptionCreated(WebHookEvent):
    HANDLER_KEY: ClassVar = ("BILLING.SUBSCRIPTION.CREATED", "subscription", "2.0")
    resource: WebHookSubscriptionResourceV2


class WebHookEventSubscriptionExpired(WebHookEvent):
    HANDLER_KEY: ClassVar = ("BILLING.SUBSCRIPTION.EXPIRED", "subscription", "2.0")
    resource: WebHookSubscriptionResourceV2


class WebHookEventSubscriptionCancelled(WebHookEvent):
    HANDLER_KEY: ClassVar = ("BILLING.SUBSCRIPTION.CANCELLED", "subscription", "2.0")
    resource: WebHookSubscriptionResourceV2


class WebHookEventSubscriptionPaymentFailed(WebHookEvent):
    HANDLER_KEY: ClassVar = ("BILLING.SUBSCRIPTION.PAYMENT.FAILED", "subscription", "2.0")
    resource: WebHookSubscriptionResourceV2


class WebHookEventSaleCompleted(WebHookEvent):
    HANDLER_KEY: ClassVar = ("PAYMENT.SALE.COMPLETED", "sale", "1.0")
    resource: WebHookSaleResource


class WebHookEventSaleReversed(WebHookEvent):
    HANDLER_KEY: ClassVar = ("PAYMENT.SALE.REVERSED", "sale", "1.0")
    resource: WebHookSaleResource


class WebHookEventSaleRefunded(WebHookEvent):
    HANDLER_KEY: ClassVar = ("PAYMENT.SALE.REFUNDED", "sale", "1.0")
    resource: WebHookSaleResource


class WebHookEventPlanCreated(WebHookEvent):
    HANDLER_KEY: ClassVar = ("BILLING.PLAN.CREATED", "plan", "2.0")
    resource: WebHookPlanResourceV2


class WebHookEventPlanUpdated(WebHookEvent):
    HANDLER_KEY: ClassVar = ("BILLING.PLAN.UPDATED", "plan", "2.0")
    resource: WebHookPlanResourceV2
