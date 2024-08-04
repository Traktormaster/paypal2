import asyncio
import os
from collections import deque
from typing import Annotated

from fastapi import Depends

from paypal2.client import PayPalApiClient
from paypal2.integration.deps import PayPalDeps
from paypal2.models.common import MonetaryValue, PlanPricingModel, PlanFrequency
from paypal2.models.plan import PlanCreate, PlanBillingCycle, PlanPaymentPreferences
from paypal2.models.product import ProductCreate


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
        plan_list = await pp.plan_list()
        for plan in plan_list.plans:
            if plan.name == plan_name and plan.product_id == product_id:
                break
        else:
            plan = None
        if plan is None:
            product = await pp.product_details(product_id)
            if product is None:
                await pp.product_create(
                    ProductCreate(id=product_id, name="digital subscription plan for testing", type="DIGITAL")
                )
            plan = await pp.plan_create(
                PlanCreate(
                    product_id=product_id,
                    name=plan_name,
                    billing_cycles=[
                        PlanBillingCycle(
                            tenure_type="REGULAR",
                            sequence=1,
                            total_cycles=0,
                            pricing_scheme=PlanPricingModel(fixed_price=MonetaryValue(currency_code="USD", value="6")),
                            frequency=PlanFrequency(interval_unit="MONTH", interval_count=1),
                        ),
                    ],
                    payment_preferences=PlanPaymentPreferences(
                        setup_fee=MonetaryValue(currency_code="USD", value="0"),
                    ),
                )
            )
        cls.PLAN_ID = plan_id = plan.id
        if (await pp.plan_details(plan_id)) is None:
            raise Exception("Failed to find/setup test plan")

    @classmethod
    async def close(cls):
        cls.WEBHOOK_RESULTS.clear()
        await cls.close_paypal()


PayPalDep = Annotated[PayPalApiClient, Depends(GlobalDeps.get_paypal)]
WebHookResults = Annotated[deque, Depends(lambda: GlobalDeps.WEBHOOK_RESULTS)]
