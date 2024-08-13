from typing import Optional

import aiohttp

from paypal2.client import PayPalApiClient
from paypal2.models.common import (
    PlanBillingCycle,
    MonetaryValue,
    PlanPricingModel,
    PlanFrequency,
    PlanPaymentPreferences,
)
from paypal2.models.plan import PlanDetails, PlanCreate
from paypal2.models.product import ProductCreate


async def ensure_simple_product_plan(
    pp: PayPalApiClient,
    product_id: str,
    plan_name: str,
    product_name: str = "digital subscription plan for testing",
    plan_fixed_price=MonetaryValue(currency_code="USD", value="6"),
    plan_frequency=PlanFrequency(interval_unit="MONTH", interval_count=1),
    plan_setup_fee=MonetaryValue(currency_code="USD", value="0"),
) -> Optional[PlanDetails]:
    """
    Subscription plans should be managed on the PayPal business UI usually.
    This code is mostly provided here for conveniently creating a specific plan-setup during testing.
    """
    if plan_fixed_price.currency_code != plan_setup_fee.currency_code:
        if float(plan_setup_fee.value) == 0:
            plan_setup_fee = MonetaryValue(currency_code=plan_fixed_price.currency_code, value="0")
        else:
            raise ValueError("currency_code must match for price and setup fee")
    try:
        plan_list = await pp.plan_list(product_id, page_size=20)
        for plan in plan_list.plans:
            if plan.name == plan_name and plan.product_id == product_id:
                break
        else:
            plan = None
    except aiohttp.ClientResponseError as e:
        if e.status != 404:
            raise
        plan = None
    if plan is None:
        product = await pp.product_details(product_id)
        if product is None:
            await pp.product_create(ProductCreate(id=product_id, name=product_name, type="DIGITAL"))
        plan = await pp.plan_create(
            PlanCreate(
                product_id=product_id,
                name=plan_name,
                billing_cycles=[
                    PlanBillingCycle(
                        tenure_type="REGULAR",
                        sequence=1,
                        total_cycles=0,
                        pricing_scheme=PlanPricingModel(fixed_price=plan_fixed_price),
                        frequency=plan_frequency,
                    ),
                ],
                payment_preferences=PlanPaymentPreferences(setup_fee=plan_setup_fee),
            )
        )
    plan_id = plan.id
    return await pp.plan_details(plan_id)
