from collections import deque
from typing import Any

from paypal2.models.hook import WebHookEventSubscriptionCreated, WebHookEventSaleCompleted, WebHookEvent


async def webhook_event_subscription_created(event: WebHookEventSubscriptionCreated, context: dict[str, Any]) -> Any:
    whr: deque = context["whr"]
    whr.append({"key": event.HANDLER_KEY, "event": event.model_dump()})
    return whr[-1]


async def webhook_event_sale_completed(event: WebHookEventSaleCompleted, context: dict[str, Any]) -> Any:
    whr: deque = context["whr"]
    whr.append({"key": event.HANDLER_KEY, "event": event.model_dump()})
    return whr[-1]


async def webhook_event_fallback(event: WebHookEvent, context: dict[str, Any]) -> Any:
    whr: deque = context["whr"]
    whr.append({"key": event.HANDLER_KEY, "event": event.model_dump()})
    return whr[-1]


WEBHOOK_HANDLERS = {
    WebHookEventSubscriptionCreated: webhook_event_subscription_created,
    WebHookEventSaleCompleted: webhook_event_sale_completed,
    WebHookEvent: webhook_event_fallback,
}
