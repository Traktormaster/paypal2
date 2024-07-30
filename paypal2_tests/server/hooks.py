from collections import deque
from typing import Any

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


async def webhook_event_debug(event: WebHookEvent, context: dict[str, Any]) -> Any:
    whr: deque = context["whr"]
    whr.append({"key": event.HANDLER_KEY, "event": event.model_dump()})
    return whr[-1]


WEBHOOK_HANDLERS = {
    WebHookEventSubscriptionCreated: webhook_event_debug,
    WebHookEventSubscriptionExpired: webhook_event_debug,
    WebHookEventSubscriptionCancelled: webhook_event_debug,
    WebHookEventSubscriptionPaymentFailed: webhook_event_debug,
    WebHookEventSaleCompleted: webhook_event_debug,
    WebHookEventSaleReversed: webhook_event_debug,
    WebHookEventSaleRefunded: webhook_event_debug,
    WebHookEventPlanCreated: webhook_event_debug,
    WebHookEventPlanUpdated: webhook_event_debug,
    WebHookEvent: webhook_event_debug,
}
