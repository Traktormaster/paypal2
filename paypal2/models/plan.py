from datetime import datetime
from typing import Optional, Literal

from pydantic import BaseModel, Field

from paypal2.models.common import HATEOASLink, PlanBillingCycle, PlanPaymentPreferences, PlanTaxes


class PlanMinimalResponse(BaseModel):
    id: str
    status: Literal["CREATED", "INACTIVE", "ACTIVE"] = Field(min_length=1, max_length=24, default="ACTIVE")
    links: list[HATEOASLink]


class _PlanCommon(BaseModel):
    product_id: str = Field(min_length=22, max_length=22)
    name: str = Field(min_length=1, max_length=127)
    status: Literal["CREATED", "INACTIVE", "ACTIVE"] = Field(min_length=1, max_length=24, default="ACTIVE")
    description: Optional[str] = Field(min_length=1, max_length=127, default=None)
    billing_cycles: Optional[list[PlanBillingCycle]] = Field(min_length=1, max_length=12, default=None)
    payment_preferences: Optional[PlanPaymentPreferences] = None
    taxes: Optional[PlanTaxes] = None


class PlanCreate(_PlanCommon):
    payment_preferences: PlanPaymentPreferences


class PlanDetails(_PlanCommon):
    id: str = Field(min_length=26, max_length=26)
    create_time: Optional[datetime] = None
    update_time: Optional[datetime] = None
    # todo quantity_supported
    # todo links


class PlanListPlan(_PlanCommon):
    id: str = Field(min_length=26, max_length=26)
    create_time: Optional[datetime] = None
    update_time: Optional[datetime] = None
    # todo quantity_supported
    # todo links


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
