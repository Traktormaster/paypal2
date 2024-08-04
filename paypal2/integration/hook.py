from typing import Any, Optional

from paypal2.client import PayPalApiClient
from paypal2.hook import PayPalWebHookProcessorBase
from paypal2.models.common import PlanBillingCycle
from paypal2.models.hook import (
    WebHookEventCaptureReversed,
    WebHookEventCaptureRefunded,
    WebHookEventSubscriptionCreated,
    WebHookEventSubscriptionExpired,
    WebHookEventSubscriptionCancelled,
    WebHookEventSubscriptionPaymentFailed,
    WebHookEventSaleCompleted,
    WebHookEventSaleReversed,
    WebHookEventSaleRefunded,
    WebHookEventPlanCreated,
    WebHookEventPlanUpdated,
    WebHookSaleResource,
    WebHookSubscriptionResourceV2,
    WebHookEventSubscriptionActivated,
    WebHookEventSubscriptionSuspended,
)
from paypal2.models.payment import CapturedPayment
from paypal2.utility import get_regular_billing_cycle


class AbstractPayPalWebHookProcessor(PayPalWebHookProcessorBase):
    """
    WebHook processor class with some general pre-processing and improved handler logic.

    The extended logic relies on the custom_id being used for subscriptions and the server being able to decode the
    identity of the subscribing entity and the service being purchased.

    NOTE: This can't be used with simulated webhook messages, as they do not provide real ids for external entities.
    """

    __slots__ = ("pp",)

    def __init__(self, pp: PayPalApiClient):
        PayPalWebHookProcessorBase.__init__(self)
        self.pp = pp

    async def _get_payment_details_with_custom_id(
        self, resource: WebHookSubscriptionResourceV2 | WebHookSaleResource
    ) -> Optional[CapturedPayment]:
        captured_payment = await self.pp.captured_payment_details(resource.id)
        if captured_payment and captured_payment.custom_id:
            return captured_payment

    # async def event_capture_completed(self, event: WebHookEventCaptureCompleted) -> Any:
    #     pass

    async def event_capture_reversed(self, event: WebHookEventCaptureReversed) -> Any:
        return await self._revoke_order(event)

    async def event_capture_refunded(self, event: WebHookEventCaptureRefunded) -> Any:
        return await self._revoke_order(event)

    async def event_subscription_created(self, event: WebHookEventSubscriptionCreated) -> Any:
        if event.resource.custom_id:
            return await self._associate_subscription(event)

    async def event_subscription_activated(self, event: WebHookEventSubscriptionActivated) -> Any:
        if event.resource.custom_id:
            return await self._track_subscription(event)

    async def event_subscription_suspended(self, event: WebHookEventSubscriptionSuspended) -> Any:
        if event.resource.custom_id:
            return await self._track_subscription(event)

    async def event_subscription_expired(self, event: WebHookEventSubscriptionExpired) -> Any:
        if event.resource.custom_id:
            return await self._dissociate_subscription(event)

    async def event_subscription_cancelled(self, event: WebHookEventSubscriptionCancelled) -> Any:
        if event.resource.custom_id:
            return await self._dissociate_subscription(event)

    async def event_subscription_payment_failed(self, event: WebHookEventSubscriptionPaymentFailed) -> Any:
        if event.resource.custom_id:
            return await self._warn_subscription_failure(event)

    async def event_sale_completed(self, event: WebHookEventSaleCompleted) -> Any:
        payment_details = await self._get_payment_details_with_custom_id(event.resource)
        if payment_details and payment_details.status == "COMPLETED":
            # NOTE: Not sure if status can be anything but "COMPLETED", or what should be done then.
            return await self._grant_subscription(event, payment_details)

    async def event_sale_reversed(self, event: WebHookEventSaleReversed) -> Any:
        payment_details = await self._get_payment_details_with_custom_id(event.resource)
        if payment_details:
            return await self._revoke_subscription(event, payment_details)

    async def event_sale_refunded(self, event: WebHookEventSaleRefunded) -> Any:
        payment_details = await self._get_payment_details_with_custom_id(event.resource)
        if payment_details:
            return await self._revoke_subscription(event, payment_details)

    async def event_plan_created(self, event: WebHookEventPlanCreated) -> Any:
        regular_bc = get_regular_billing_cycle(event.resource.billing_cycles)
        if regular_bc:
            return await self._track_plan_pricing(event, regular_bc)

    async def event_plan_updated(self, event: WebHookEventPlanUpdated) -> Any:
        regular_bc = get_regular_billing_cycle(event.resource.billing_cycles)
        if regular_bc:
            return await self._track_plan_pricing(event, regular_bc)

    # async def event_fallback(self, event: WebHookEvent) -> Any:
    #     pass

    async def _revoke_order(self, event: WebHookEventCaptureReversed | WebHookEventCaptureRefunded) -> Any:
        """
        Revoke the ordered service denoted by the id of the payment.
        """
        raise NotImplementedError()

    async def _associate_subscription(self, event: WebHookEventSubscriptionCreated) -> Any:
        """
        The relationship among subscription-id, plan-id, custom-id and likely user/party must be recorded so later
        "grant_subscription" events can look up all the information from a "custom_id".
        """
        raise NotImplementedError()

    async def _track_subscription(
        self, event: WebHookEventSubscriptionActivated | WebHookEventSubscriptionSuspended
    ) -> Any:
        """
        For tracking a subscription status on the server.
        """
        raise NotImplementedError()

    async def _dissociate_subscription(
        self, event: WebHookEventSubscriptionExpired | WebHookEventSubscriptionCancelled
    ) -> Any:
        """
        For tracking a subscription on the server, mark or discard the subscription resource-id from the subscriber
        denoted by the custom_id.
        """
        raise NotImplementedError()

    async def _warn_subscription_failure(self, event: WebHookEventSubscriptionPaymentFailed) -> Any:
        """
        Notify the subscriber denoted by the custom_id that their subscription payment could not be processed.
        """
        raise NotImplementedError()

    async def _grant_subscription(self, event: WebHookEventSaleCompleted, payment_details: CapturedPayment) -> Any:
        """
        Grant the subscribed service denoted by the custom_id since created_time, tracked as the id of the payment.
        """
        raise NotImplementedError()

    async def _revoke_subscription(
        self, event: WebHookEventSaleReversed | WebHookEventSaleRefunded, payment_details: CapturedPayment
    ) -> Any:
        """
        Revoke the subscribed service denoted by the custom_id and tracked as the id of the payment.
        """
        raise NotImplementedError()

    async def _track_plan_pricing(
        self, event: WebHookEventPlanCreated | WebHookEventPlanUpdated, billing_cycle: PlanBillingCycle
    ) -> Any:
        """
        Track the property changes of the plan resource. The "REGULAR" billing cycle is selected for convenience.
        NOTE: The server must query and update the tracked plans on startup using the plan_details(...) api and only
        rely on the webhooks to keep the state synced.
        """
        raise NotImplementedError()
