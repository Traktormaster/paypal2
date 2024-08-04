from typing import Optional, Literal, ClassVar

from pydantic import BaseModel, Field


class MonetaryValue(BaseModel):
    currency_code: str = Field(min_length=3, max_length=3)
    value: str = Field(max_length=32)


class HATEOASLink(BaseModel):
    href: str
    rel: str
    method: Optional[str] = None


class RelatedIds(BaseModel):
    order_id: Optional[str] = None
    authorization_id: Optional[str] = None
    capture_id: Optional[str] = None


class PaymentSupplementaryData(BaseModel):
    related_ids: Optional[RelatedIds] = None


class PlanPaymentPreferences(BaseModel):
    auto_bill_outstanding: Optional[bool] = True
    setup_fee_failure_action: Optional[Literal["CONTINUE", "CANCEL"]] = "CANCEL"
    payment_failure_threshold: Optional[int] = 0
    setup_fee: MonetaryValue


class PlanPricingTier(BaseModel):
    starting_quantity: str
    ending_quantity: Optional[str] = None
    amount: MonetaryValue


class PlanPricingModel(BaseModel):
    pricing_model: Optional[Literal["VOLUME", "TIERED"]] = None
    tiers: Optional[list[PlanPricingTier]] = None
    fixed_price: Optional[MonetaryValue] = None


class PlanFrequency(BaseModel):
    interval_unit: Literal["DAY", "WEEK", "MONTH", "YEAR"]
    interval_count: int = Field(ge=1, le=365, default=1)  # NOTE: maximum depends on interval_unit

    INTERVAL_DAYS: ClassVar = {"DAY": 1, "WEEK": 7, "MONTH": 31, "YEAR": 365}

    @property
    def interval_as_days(self) -> int:
        return self.INTERVAL_DAYS[self.interval_unit] * self.interval_count


class PlanBillingCycle(BaseModel):
    tenure_type: Literal["REGULAR", "TRIAL"]
    sequence: int = Field(ge=1, le=99)
    total_cycles: int = Field(ge=0, le=999, default=1)  # 0 infinite
    pricing_scheme: Optional[PlanPricingModel]  # trial needs no pricing
    frequency: PlanFrequency


class PlanTaxes(BaseModel):
    inclusive: bool = True
    percentage: str = Field(pattern=r"^((-?[0-9]+)|(-?([0-9]+)?[.][0-9]+))$")
