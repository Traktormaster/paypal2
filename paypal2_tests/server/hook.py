from collections import deque
from typing import Any

from paypal2.client import PayPalApiClient
from paypal2.hook import PayPalWebHookProcessorBase
from paypal2.integration.hook import AbstractPayPalWebHookProcessor
from paypal2.models.common import PlanBillingCycle
from paypal2.models.hook import (
    WebHookEventSubscriptionCreated,
    WebHookEventSubscriptionExpired,
    WebHookEventSubscriptionCancelled,
    WebHookEventSubscriptionPaymentFailed,
    WebHookEventSaleCompleted,
    WebHookEventSaleReversed,
    WebHookEventSaleRefunded,
    WebHookEventPlanCreated,
    WebHookEventPlanUpdated,
    WebHookEvent,
)
from paypal2.models.payment import CapturedPayment


class DebugPayPalWebHookProcessor(AbstractPayPalWebHookProcessor):
    __slots__ = ("whr",)

    def __init__(self, pp: PayPalApiClient, whr: deque):
        AbstractPayPalWebHookProcessor.__init__(self, pp)
        self.whr = whr

    async def _associate_subscription(self, event: WebHookEventSubscriptionCreated) -> Any:
        self.whr.append({"handle": "associate_subscription", "key": event.HANDLER_KEY, "event": event.model_dump()})
        return self.whr[-1]

    async def _dissociate_subscription(
        self, event: WebHookEventSubscriptionExpired | WebHookEventSubscriptionCancelled
    ) -> Any:
        self.whr.append({"handle": "dissociate_subscription", "key": event.HANDLER_KEY, "event": event.model_dump()})
        return self.whr[-1]

    async def _warn_subscription_failure(self, event: WebHookEventSubscriptionPaymentFailed) -> Any:
        self.whr.append({"handle": "warn_subscription_failure", "key": event.HANDLER_KEY, "event": event.model_dump()})
        return self.whr[-1]

    async def _grant_subscription(self, event: WebHookEventSaleCompleted, payment_details: CapturedPayment) -> Any:
        self.whr.append(
            {
                "handle": "grant_subscription",
                "key": event.HANDLER_KEY,
                "event": event.model_dump(),
                "payment_details": payment_details.model_dump(),
            }
        )
        return self.whr[-1]

    async def _revoke_subscription(
        self, event: WebHookEventSaleReversed | WebHookEventSaleRefunded, payment_details: CapturedPayment
    ) -> Any:
        self.whr.append(
            {
                "handle": "revoke_subscription",
                "key": event.HANDLER_KEY,
                "event": event.model_dump(),
                "payment_details": payment_details.model_dump(),
            }
        )
        return self.whr[-1]

    async def _track_plan_pricing(
        self, event: WebHookEventPlanCreated | WebHookEventPlanUpdated, billing_cycle: PlanBillingCycle
    ) -> Any:
        self.whr.append(
            {
                "handle": "track_plan_pricing",
                "key": event.HANDLER_KEY,
                "event": event.model_dump(),
                "billing_cycle": billing_cycle.model_dump(),
            }
        )
        return self.whr[-1]

    async def event_fallback(self, event: WebHookEvent) -> Any:
        self.whr.append({"handle": "event_fallback", "key": event.HANDLER_KEY, "event": event.model_dump()})
        return self.whr[-1]


class DebugPayPalWebHookProcessorBase(PayPalWebHookProcessorBase):
    __slots__ = ("whr",)

    def __init__(self, whr: deque):
        PayPalWebHookProcessorBase.__init__(self)
        self.whr = whr

    async def event_subscription_created(self, event: WebHookEventSubscriptionCreated) -> Any:
        self.whr.append({"key": event.HANDLER_KEY, "event": event.model_dump()})
        return self.whr[-1]

    async def event_subscription_expired(self, event: WebHookEventSubscriptionExpired) -> Any:
        self.whr.append({"key": event.HANDLER_KEY, "event": event.model_dump()})
        return self.whr[-1]

    async def event_subscription_cancelled(self, event: WebHookEventSubscriptionCancelled) -> Any:
        self.whr.append({"key": event.HANDLER_KEY, "event": event.model_dump()})
        return self.whr[-1]

    async def event_subscription_payment_failed(self, event: WebHookEventSubscriptionPaymentFailed) -> Any:
        self.whr.append({"key": event.HANDLER_KEY, "event": event.model_dump()})
        return self.whr[-1]

    async def event_sale_completed(self, event: WebHookEventSaleCompleted) -> Any:
        self.whr.append({"key": event.HANDLER_KEY, "event": event.model_dump()})
        return self.whr[-1]

    async def event_sale_reversed(self, event: WebHookEventSaleReversed) -> Any:
        self.whr.append({"key": event.HANDLER_KEY, "event": event.model_dump()})
        return self.whr[-1]

    async def event_sale_refunded(self, event: WebHookEventSaleRefunded) -> Any:
        self.whr.append({"key": event.HANDLER_KEY, "event": event.model_dump()})
        return self.whr[-1]

    async def event_plan_created(self, event: WebHookEventPlanCreated) -> Any:
        self.whr.append({"key": event.HANDLER_KEY, "event": event.model_dump()})
        return self.whr[-1]

    async def event_plan_updated(self, event: WebHookEventPlanUpdated) -> Any:
        self.whr.append({"key": event.HANDLER_KEY, "event": event.model_dump()})
        return self.whr[-1]

    async def event_fallback(self, event: WebHookEvent) -> Any:
        self.whr.append({"key": event.HANDLER_KEY, "event": event.model_dump()})
        return self.whr[-1]