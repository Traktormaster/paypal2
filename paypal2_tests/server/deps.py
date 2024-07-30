import os
from collections import deque
from typing import Annotated

from fastapi import Depends

from paypal2.client import PayPalApiClient
from paypal2.models.common import MonetaryValue
from paypal2.models.plan import PlanCreate, BillingCycle, Frequency, PricingModel, PlanPaymentPreferences
from paypal2.models.product import ProductCreate
from paypal2_tests.server.hooks import WEBHOOK_HANDLERS


class GlobalDeps:
    PAYPAL: PayPalApiClient = None
    WEBHOOK_RESULTS = deque()
    PRODUCT_ID: str = None
    PLAN_NAME: str = None
    PLAN_ID: str = None

    @classmethod
    async def setup(cls):
        client_id = os.environ["PAYPAL2_TESTING_CLIENT_ID"]
        client_secret = os.environ["PAYPAL2_TESTING_CLIENT_SECRET"]
        webhook_id = os.environ.get("PAYPAL2_TESTING_WEBHOOK_ID", "WEBHOOK_ID")  # "WEBHOOK_ID" is for simulated calls
        pp = PayPalApiClient(
            client_id,
            client_secret,
            url_base=PayPalApiClient.SANDBOX_URL_BASE,
            webhook_id=webhook_id,
            webhook_handlers=WEBHOOK_HANDLERS,
        )
        await pp.setup()
        cls.PAYPAL = pp
        await cls._setup_subscription_plan(pp)

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
                        BillingCycle(
                            tenure_type="REGULAR",
                            sequence=1,
                            total_cycles=0,
                            pricing_scheme=PricingModel(fixed_price=MonetaryValue(currency_code="USD", value="6")),
                            frequency=Frequency(interval_unit="MONTH", interval_count=1),
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
        if cls.PAYPAL:
            await cls.PAYPAL.close()

    @classmethod
    def get_paypal(cls) -> PayPalApiClient:
        pp = cls.PAYPAL
        if not pp:
            raise Exception("PAYPAL dep has not been set up")
        return pp


PayPalDep = Annotated[PayPalApiClient, Depends(GlobalDeps.get_paypal)]
WebHookResults = Annotated[deque, Depends(lambda: GlobalDeps.WEBHOOK_RESULTS)]
