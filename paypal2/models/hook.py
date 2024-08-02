from datetime import datetime
from typing import Optional, ClassVar

from pydantic import BaseModel, Field

from paypal2.models.common import HATEOASLink, PlanBillingCycle, PlanPaymentPreferences, PlanTaxes, MonetaryValue, \
    PaymentSupplementaryData


class WebHookEvent(BaseModel):
    HANDLER_KEY: ClassVar[Optional[tuple[str, str, str]]] = None
    id: str
    event_type: str
    event_version: str
    resource_type: str
    resource_version: Optional[str] = None
    resource: dict
    links: list[HATEOASLink]


class WebHookCaptureResourceV2(BaseModel):
    id: str
    status: str
    amount: Optional[MonetaryValue] = None
    supplementary_data: Optional[PaymentSupplementaryData] = None
    create_time: Optional[datetime] = None
    update_time: Optional[datetime] = None
    links: list[HATEOASLink]
    # todo seller_protection
    # todo seller_receivable_breakdown
    # todo payee
    # todo final_capture


class WebHookSubscriptionResourceV2(BaseModel):
    id: str
    status: str
    status_update_time: Optional[str] = None
    plan_id: str
    custom_id: Optional[str] = None
    start_time: Optional[str] = None
    auto_renewal: Optional[bool] = None
    create_time: Optional[datetime] = None
    update_time: Optional[datetime] = None
    links: list[HATEOASLink]
    # todo quantity
    # todo shipping_amount
    # todo subscriber
    # todo billing_info


class WebHookPlanResourceV2(BaseModel):
    id: str
    product_id: str
    status: str
    name: Optional[str] = None
    description: Optional[str] = None
    usage_type: Optional[str] = None
    links: list[HATEOASLink]
    billing_cycles: Optional[list[PlanBillingCycle]] = None
    payment_preferences: Optional[PlanPaymentPreferences] = None
    taxes: Optional[PlanTaxes] = None
    create_time: Optional[datetime] = None
    update_time: Optional[datetime] = None


class MonetaryTotal(BaseModel):
    currency: str = Field(max_length=5)
    total: str = Field(max_length=50)
    details: Optional[dict] = None


class WebHookSaleResource(BaseModel):
    id: str
    state: str
    amount: Optional[MonetaryTotal] = None
    links: list[HATEOASLink]
    create_time: Optional[datetime] = None
    update_time: Optional[datetime] = None  # for complete and refund
    # todo sale_id for refund
    # todo parent_payment for complete, refund
    # todo clearing_time for complete
    # todo payment_mode for complete
    # todo protection_eligibility for complete
    # todo protection_eligibility_type for complete

    # NOTE: There is a "custom" field here with the value of the subscription's "custom_id" if any, but there is no
    # mention of this field in the official documentation, so I'm not sure if we should rely on it at all. The web-hook
    # processing of the integration layer does not utilize this, but queries the related captured-payment details which
    # has an official "custom_id" field.
    custom: Optional[str] = None


class WebHookEventCaptureCompleted(WebHookEvent):
    HANDLER_KEY: ClassVar = ("PAYMENT.CAPTURE.COMPLETED", "capture", "2.0")
    resource: WebHookCaptureResourceV2


class WebHookEventCaptureReversed(WebHookEvent):
    HANDLER_KEY: ClassVar = ("PAYMENT.CAPTURE.REVERSED", "capture", "2.0")
    resource: WebHookCaptureResourceV2


class WebHookEventCaptureRefunded(WebHookEvent):
    HANDLER_KEY: ClassVar = ("PAYMENT.CAPTURE.REFUNDED", "capture", "2.0")
    resource: WebHookCaptureResourceV2


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
