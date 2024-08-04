from paypal2.client import PayPalApiClient


class PayPalDeps:
    PAYPAL: PayPalApiClient = None

    @classmethod
    async def setup_paypal(cls, *args, **kwargs):
        pp = PayPalApiClient(*args, **kwargs)
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
