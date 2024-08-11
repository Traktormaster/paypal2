import asyncio
import os
from collections import deque
from typing import Annotated

from fastapi import Depends

from paypal2.client import PayPalApiClient
from paypal2.integration.deps import PayPalDeps
from paypal2.misc import ensure_simple_product_plan


class GlobalDeps(PayPalDeps):
    PAYPAL: PayPalApiClient = None
    WEBHOOK_RESULTS: deque = None
    PRODUCT_ID: str = None
    PLAN_NAME: str = None
    PLAN_ID: str = None
    ACID_LOCK: asyncio.Lock = None

    @classmethod
    async def setup(cls):
        cls.WEBHOOK_RESULTS = deque()
        cls.ACID_LOCK = asyncio.Lock()
        await cls.setup_paypal(
            os.environ["PAYPAL2_TESTING_CLIENT_ID"],
            os.environ["PAYPAL2_TESTING_CLIENT_SECRET"],
            webhook_id=os.environ.get("PAYPAL2_TESTING_WEBHOOK_ID", "WEBHOOK_ID"),  # constant is for simulated calls
        )
        cls.PAYPAL.url_base = cls.PAYPAL.SANDBOX_URL_BASE
        await cls._setup_subscription_plan(cls.PAYPAL)

    @classmethod
    async def _setup_subscription_plan(cls, pp: PayPalApiClient):
        cls.PRODUCT_ID = product_id = os.environ.get("PAYPAL2_TESTING_PRODUCT_ID", "TEST-PRODUCT-123456789")
        cls.PLAN_NAME = plan_name = "TEST-PLAN-123456789ABCDEF0"
        # Subscription plans should be managed on the business UI, for testing we simply setup/check a specific one.
        plan = await ensure_simple_product_plan(pp, product_id, plan_name)
        if plan is None:
            raise Exception("Failed to find/setup test plan")
        cls.PLAN_ID = plan.id

    @classmethod
    async def close(cls):
        cls.WEBHOOK_RESULTS.clear()
        await cls.close_paypal()


PayPalDep = Annotated[PayPalApiClient, Depends(GlobalDeps.get_paypal)]
WebHookResults = Annotated[deque, Depends(lambda: GlobalDeps.WEBHOOK_RESULTS)]
