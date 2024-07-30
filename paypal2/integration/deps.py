from typing import Optional

from paypal2.client import PayPalApiClient, WebHookHandlers


class PayPalDeps:
    PAYPAL: PayPalApiClient = None

    @classmethod
    async def setup_paypal(
        cls,
        client_id: str,
        client_secret: str,
        webhook_id: Optional[str] = None,
        webhook_handlers: Optional[WebHookHandlers] = None,
    ):
        pp = PayPalApiClient(client_id, client_secret, webhook_id=webhook_id, webhook_handlers=webhook_handlers)
        await pp.setup()
        cls.PAYPAL = pp
        return pp

    @classmethod
    async def close_paypal(cls):
        if cls.PAYPAL:
            await cls.PAYPAL.close()

    @classmethod
    def get_paypal(cls) -> PayPalApiClient:
        pp = cls.PAYPAL
        if not pp:
            raise Exception("PAYPAL dep has not been set up")
        return pp
