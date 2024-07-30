# TODO: WIP

from typing import Any

from paypal2.client import PayPalApiClient, WebHookHandlers
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


class PayPalWebHooks:
    def __init__(self):
        self.handlers: WebHookHandlers = self._init_handlers()

    def _init_handlers(self) -> WebHookHandlers:
        """
        Filter default handlers to only be present if they are overridden.
        Override this method to customize/replace this behaviour.
        """
        cls = type(self)
        return {
            e: h
            for e, h in self._all_handlers().items()
            if getattr(cls, h.__name__) == getattr(PayPalWebHooks, h.__name__)
        }

    def _all_handlers(self) -> WebHookHandlers:
        return {
            WebHookEventSubscriptionCreated: self.event_subscription_created,
            WebHookEventSubscriptionExpired: self.event_subscription_expired,
            WebHookEventSubscriptionCancelled: self.event_subscription_cancelled,
            WebHookEventSubscriptionPaymentFailed: self.event_subscription_payment_failed,
            WebHookEventSaleCompleted: self.event_sale_completed,
            WebHookEventSaleReversed: self.event_sale_reversed,
            WebHookEventSaleRefunded: self.event_sale_refunded,
            WebHookEventPlanCreated: self.event_plan_created,
            WebHookEventPlanUpdated: self.event_plan_updated,
            WebHookEvent: self.event_fallback,
        }

    async def event_subscription_created(self, event: WebHookEventSubscriptionCreated, context: dict[str, Any]) -> Any:
        pass

    async def event_subscription_expired(self, event: WebHookEventSubscriptionExpired, context: dict[str, Any]) -> Any:
        pass

    async def event_subscription_cancelled(
        self, event: WebHookEventSubscriptionCancelled, context: dict[str, Any]
    ) -> Any:
        pass

    async def event_subscription_payment_failed(
        self, event: WebHookEventSubscriptionPaymentFailed, context: dict[str, Any]
    ) -> Any:
        pass

    async def event_sale_completed(self, event: WebHookEventSaleCompleted, context: dict[str, Any]) -> Any:
        pp: PayPalApiClient = context["pp"]
        captured_payment = await pp.captured_payment_details(event.resource.id)
        if not captured_payment or not captured_payment.custom_id:
            pass  # TODO

    async def event_sale_reversed(self, event: WebHookEventSaleReversed, context: dict[str, Any]) -> Any:
        pass

    async def event_sale_refunded(self, event: WebHookEventSaleRefunded, context: dict[str, Any]) -> Any:
        pass

    async def event_plan_created(self, event: WebHookEventPlanCreated, context: dict[str, Any]) -> Any:
        pass

    async def event_plan_updated(self, event: WebHookEventPlanUpdated, context: dict[str, Any]) -> Any:
        pass

    async def event_fallback(self, event: WebHookEvent, context: dict[str, Any]) -> Any:
        pass
