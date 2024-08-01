from typing import TypeVar, Any, Awaitable, Callable, Type

from paypal2.models.hook import (
    WebHookEvent,
    WebHookEventSubscriptionCreated,
    WebHookEventSubscriptionExpired,
    WebHookEventSubscriptionCancelled,
    WebHookEventSubscriptionPaymentFailed,
    WebHookEventSaleCompleted,
    WebHookEventSaleReversed,
    WebHookEventSaleRefunded,
    WebHookEventPlanCreated,
    WebHookEventPlanUpdated,
)

_WebHookEventType = TypeVar("_WebHookEventType", bound=WebHookEvent)
WebHookHandler = Callable[[_WebHookEventType], Awaitable[Any]]
WebHookHandlers = dict[Type[_WebHookEventType], WebHookHandler]


class PayPalWebHookProcessorBase:
    """
    WebHook processor class for processing the raw events freely.
    """

    __slots__ = ("webhook_handlers",)

    def __init__(self):
        self.webhook_handlers = {e.HANDLER_KEY: (e, h) for e, h in self._init_handlers().items()}

    def _init_handlers(self) -> WebHookHandlers:
        """
        Override this method to remove or extend the used handlers.
        """
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

    async def call(self, data: dict) -> Any:
        """
        Automatic WebHook data handler selection and processing.
        """
        handler_key = (data.get("event_type"), data.get("resource_type"), data.get("resource_version", "1.0"))
        event_handler = self.webhook_handlers.get(handler_key)
        if not event_handler:
            event_handler = self.webhook_handlers.get(None)  # try fallback if it is registered
            if not event_handler:
                return
        event = event_handler[0].model_validate(data)
        return await event_handler[1](event)

    async def event_subscription_created(self, event: WebHookEventSubscriptionCreated) -> Any:
        pass

    async def event_subscription_expired(self, event: WebHookEventSubscriptionExpired) -> Any:
        pass

    async def event_subscription_cancelled(self, event: WebHookEventSubscriptionCancelled) -> Any:
        pass

    async def event_subscription_payment_failed(self, event: WebHookEventSubscriptionPaymentFailed) -> Any:
        pass

    async def event_sale_completed(self, event: WebHookEventSaleCompleted) -> Any:
        pass

    async def event_sale_reversed(self, event: WebHookEventSaleReversed) -> Any:
        pass

    async def event_sale_refunded(self, event: WebHookEventSaleRefunded) -> Any:
        pass

    async def event_plan_created(self, event: WebHookEventPlanCreated) -> Any:
        pass

    async def event_plan_updated(self, event: WebHookEventPlanUpdated) -> Any:
        pass

    async def event_fallback(self, event: WebHookEvent) -> Any:
        pass
