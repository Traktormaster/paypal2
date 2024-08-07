from typing import TypeVar, Any, Awaitable, Callable, Type

from paypal2.models.hook import (
    WebHookEvent,
    WebHookEventCaptureCompleted,
    WebHookEventCaptureReversed,
    WebHookEventCaptureRefunded,
    WebHookEventSubscriptionCreated,
    WebHookEventSubscriptionActivated,
    WebHookEventSubscriptionSuspended,
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
            # WebHookEventCapturePending: self.event_capture_pending,
            WebHookEventCaptureCompleted: self.event_capture_completed,
            WebHookEventCaptureReversed: self.event_capture_reversed,
            WebHookEventCaptureRefunded: self.event_capture_refunded,
            # WebHookEventCaptureDeclined: self.event_capture_declined,
            WebHookEventSubscriptionCreated: self.event_subscription_created,
            WebHookEventSubscriptionActivated: self.event_subscription_activated,
            WebHookEventSubscriptionSuspended: self.event_subscription_suspended,
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

    async def event_capture_completed(self, event: WebHookEventCaptureCompleted) -> Any:
        """
        This is mostly informational, as the capturing of the order (unless you use intent: AUTHORIZE) is
        done by direct API call.
        """

    async def event_capture_reversed(self, event: WebHookEventCaptureReversed) -> Any:
        """
        The server shall revoke the granted resource by the id of the capture or record it as denied for reference.
        """

    async def event_capture_refunded(self, event: WebHookEventCaptureRefunded) -> Any:
        """
        The server shall revoke the granted resource by the id of the capture or record it as denied for reference.
        """

    async def event_subscription_created(self, event: WebHookEventSubscriptionCreated) -> Any:
        """
        This is the first event where the new subscription-id (id), plan_id and custom_id are all present and have
        clear relations to each other. The server should record these associations for later, for example a
        sale-completed event will only connect to the subscription through the custom_id (queried from the captured
        payment endpoint).
        Tracking the subscription for a user/identity may be desired for information or performing actions like
        suspend or continue for example anyway.
        """

    async def event_subscription_activated(self, event: WebHookEventSubscriptionActivated) -> Any:
        """
        Record the subscription state change for the relevant party if it is tracked.
        """

    async def event_subscription_suspended(self, event: WebHookEventSubscriptionSuspended) -> Any:
        """
        Record the subscription state change for the relevant party if it is tracked.
        """

    async def event_subscription_expired(self, event: WebHookEventSubscriptionExpired) -> Any:
        """
        Record the subscription state change or remove the subscription from the relevant party if it is tracked,
        because it is no longer valid.
        """

    async def event_subscription_cancelled(self, event: WebHookEventSubscriptionCancelled) -> Any:
        """
        Record the subscription state change or remove the subscription from the relevant party if it is tracked,
        because it is no longer valid.
        """

    async def event_subscription_payment_failed(self, event: WebHookEventSubscriptionPaymentFailed) -> Any:
        """
        A payment was not successfully charged. This is mostly informational, the relevant party should be notified.
        The subscription may still be active or may have got suspended based on the payment_preferences of the plan.
        NOTE: It is not clear if failure of charging the setup_fee would trigger this event, but depending on
        the payment_preferences, the subscription could also be cancelled here.
        """

    async def event_sale_completed(self, event: WebHookEventSaleCompleted) -> Any:
        """
        A subscription payment has been successfully charged, grant the service/resource to the relevant party.
        """

    async def event_sale_reversed(self, event: WebHookEventSaleReversed) -> Any:
        """
        The server shall revoke the granted resource by the id of the sale or record it as denied for reference.
        """

    async def event_sale_refunded(self, event: WebHookEventSaleRefunded) -> Any:
        """
        The server shall revoke the granted resource by the id of the sale or record it as denied for reference.
        """

    async def event_plan_created(self, event: WebHookEventPlanCreated) -> Any:
        """
        The server can track the details of specific plans that are relevant for its users. This is beneficial,
        as the products and plans are primarily managed on the PayPal server/UI.
        """

    async def event_plan_updated(self, event: WebHookEventPlanUpdated) -> Any:
        """
        The server can track the details of specific plans that are relevant for its users. This is beneficial,
        as the products and plans are primarily managed on the PayPal server/UI.
        """

    async def event_fallback(self, event: WebHookEvent) -> Any:
        """
        Any event not captured by specific handlers may be processed here for introspection for example.
        """
