from typing import Optional, Literal, Union, Any

from pydantic import BaseModel, Field

from paypal2.models.common import MonetaryValue, HATEOASLink


class PlanPaymentPreferences(BaseModel):
    auto_bill_outstanding: Optional[bool] = True
    setup_fee_failure_action: Optional[Literal["CONTINUE", "CANCEL"]] = "CANCEL"
    payment_failure_threshold: Optional[int] = 0
    setup_fee: MonetaryValue


class PricingModel(BaseModel):
    # todo pricing_model: Optional[Literal["VOLUME", "TIERED"]]
    # todo tiers: Optional[list[TieredPricing]] = None
    fixed_price: Optional[MonetaryValue] = None


class Frequency(BaseModel):
    interval_unit: Literal["DAY", "WEEK", "MONTH", "YEAR"]
    interval_count: int = Field(ge=1, le=365, default=1)  # NOTE: maximum depends on interval_unit


class BillingCycle(BaseModel):
    tenure_type: Literal["REGULAR", "TRIAL"]
    sequence: int = Field(ge=1, le=99)
    total_cycles: int = Field(ge=0, le=999, default=1)  # 0 infinite
    pricing_scheme: Optional[PricingModel]  # trial needs no pricing
    frequency: Frequency


class PlanTaxes(BaseModel):
    inclusive: bool = True
    percentage: str = Field(pattern=r"^((-?[0-9]+)|(-?([0-9]+)?[.][0-9]+))$")


class PlanMinimalResponse(BaseModel):
    id: str
    status: Literal["CREATED", "INACTIVE", "ACTIVE"] = Field(min_length=1, max_length=24, default="ACTIVE")
    links: list[HATEOASLink]


class _PlanCommon(BaseModel):
    product_id: str = Field(min_length=22, max_length=22)
    name: str = Field(min_length=1, max_length=127)
    # TODO status
    description: Optional[str] = Field(min_length=1, max_length=127, default=None)
    billing_cycles: Optional[list[BillingCycle]] = Field(min_length=1, max_length=12, default=None)
    payment_preferences: Optional[PlanPaymentPreferences] = None
    taxes: Optional[PlanTaxes] = None


class PlanCreate(_PlanCommon):
    payment_preferences: PlanPaymentPreferences


class PlanDetails(_PlanCommon):
    id: str = Field(min_length=26, max_length=26)
    # todo quantity_supported
    # todo links
    # todo create_time
    # todo update_time


class PlanListPlan(_PlanCommon):
    id: str = Field(min_length=26, max_length=26)
    # todo quantity_supported
    # todo links
    # todo create_time
    # todo update_time


class PlanList(BaseModel):
    plans: list[PlanListPlan]
    total_items: Optional[int] = None
    total_pages: Optional[int] = None
    # todo links


# class PlanUpdate(BaseModel):
#     op: Literal["add", "remove", "replace", "move", "copy", "test"]
#     path: str
#     value: Optional[Any] = None
#     from_field: Optional[Any] = Field(alias="from", default=None)
