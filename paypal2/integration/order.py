from paypal2.client import PayPalApiClient
from paypal2.models.order import OrderMinimalResponse, OrdersCreate


class AbstractOrderCreateProcess:
    """
    Blueprint for implementing/performing an order creation.
    """

    def __init__(self, pp: PayPalApiClient):
        self.pp = pp

    async def run(self, request: OrdersCreate) -> OrderMinimalResponse:
        await self._validate_request(request)
        try:
            order_response = await self.pp.order_create(request)
        except Exception as e:
            await self._handle_pp_exception(e)
            raise e
        await self._complete_create(order_response)
        return order_response

    async def _validate_request(self, request: OrdersCreate):
        """
        Validate the order data and any custom server-local data related to the order.
        Raise an exception if something is not correct.
        """

    async def _handle_pp_exception(self, e: Exception):
        """
        Custom handling of a PayPal API call exception can log it for review and raise a custom exception instead.
        """

    async def _complete_create(self, order_response: OrderMinimalResponse):
        """
        Store/save the id of the created order for the relevant entity, so it can be verified to match a request to
        order capturing later.
        """
        raise NotImplementedError()


class AbstractOrderCaptureProcess:
    """
    Blueprint for implementing/performing an order capture.
    """

    def __init__(self, pp: PayPalApiClient):
        self.pp = pp

    async def run(self, order_id: str) -> OrderMinimalResponse:
        """
        Data access and processing needs strict transaction properties (ACID) over the execution for safety against
        parallel multiple invocations.
        Retrying or handling differently when the "status" of the returned order data is not "COMPLETED" is up to the
        coder.
        """
        await self._validate_order_id(order_id)
        try:
            order_response = await self.pp.order_capture(order_id)
        except Exception as e:
            await self._handle_pp_exception(e)
            raise e
        if order_response.status == "COMPLETED":
            await self._complete_capture(order_response)
        return order_response

    async def _validate_order_id(self, order_id: str):
        """
        Raise an exception if the order_id is not known/saved to the relevant entities.
        """
        raise NotImplementedError()

    async def _handle_pp_exception(self, e: Exception):
        """
        Custom handling of a PayPal API call exception can log it for review and raise a custom exception instead.
        """

    async def _complete_capture(self, order_response: OrderMinimalResponse):
        """
        Honor the captured order by granting the purchased service/thing to the user.
        Also clear the stored order_response.id so a subsequent call to _validate_order_id() will not succeed.
        """
        raise NotImplementedError()
