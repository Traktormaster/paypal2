from typing import Any, Optional

from paypal2.client import PayPalApiClient
from paypal2.hook import PayPalWebHookProcessorBase
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
    WebHookSaleResource,
    WebHookSubscriptionResourceV2,
)
from paypal2.models.payment import CapturedPayment


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

    async def event_subscription_created(self, event: WebHookEventSubscriptionCreated) -> Any:
        payment_details = await self._get_payment_details_with_custom_id(event.resource)
        if payment_details:
            return await self._associate_subscription(event, payment_details)

    async def event_subscription_expired(self, event: WebHookEventSubscriptionExpired) -> Any:
        payment_details = await self._get_payment_details_with_custom_id(event.resource)
        if payment_details:
            return await self._dissociate_subscription(event, payment_details)

    async def event_subscription_cancelled(self, event: WebHookEventSubscriptionCancelled) -> Any:
        payment_details = await self._get_payment_details_with_custom_id(event.resource)
        if payment_details:
            return await self._dissociate_subscription(event, payment_details)

    async def event_subscription_payment_failed(self, event: WebHookEventSubscriptionPaymentFailed) -> Any:
        payment_details = await self._get_payment_details_with_custom_id(event.resource)
        if payment_details:
            return await self._warn_subscription_failure(event, payment_details)

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
        for bc in event.resource.billing_cycles or []:
            if bc.tenure_type == "REGULAR":
                if bc.pricing_scheme and bc.frequency:  # these should be present always
                    return await self._track_plan_pricing(event, bc)
                break  # NOTE: At most one "REGULAR", so we can exit.

    async def event_plan_updated(self, event: WebHookEventPlanUpdated) -> Any:
        for bc in event.resource.billing_cycles or []:
            if bc.tenure_type == "REGULAR":
                if bc.pricing_scheme and bc.frequency:  # these should be present always
                    return await self._track_plan_pricing(event, bc)
                break  # NOTE: At most one "REGULAR", so we can exit.

    # async def event_fallback(self, event: WebHookEvent) -> Any:
    #     pass

    async def _associate_subscription(
        self, event: WebHookEventSubscriptionCreated, payment_details: CapturedPayment
    ) -> Any:
        """
        For tracking a subscription on the server, save the subscription resource-id to the subscriber denoted by the
        custom_id.
        """
        raise NotImplementedError()

    async def _dissociate_subscription(
        self,
        event: WebHookEventSubscriptionExpired | WebHookEventSubscriptionCancelled,
        payment_details: CapturedPayment,
    ) -> Any:
        """
        For tracking a subscription on the server, discard the subscription resource-id from the subscriber denoted by
        the custom_id.
        """
        raise NotImplementedError()

    async def _warn_subscription_failure(
        self, event: WebHookEventSubscriptionPaymentFailed, payment_details: CapturedPayment
    ) -> Any:
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
        """
        raise NotImplementedError()
