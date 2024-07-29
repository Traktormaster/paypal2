from typing import Optional

from pydantic import BaseModel, Field

from paypal2.models.common import HATEOASLink


class SubscriptionCreate(BaseModel):
    id: str = Field(min_length=26, max_length=26)
    quantity: Optional[str] = Field(min_length=1, max_length=32)
    custom_id: Optional[str] = Field(min_length=1, max_length=127)  # can be invoice id
    # todo start_time
    # todo shipping_amount
    # todo subscriber
    # todo application_context
    # todo plan


class SubscriptionMinimalResponse(BaseModel):
    id: str
    status: str
    links: list[HATEOASLink]


class SubscriptionDetails(BaseModel):
    id: str = Field(min_length=3, max_length=50)
    plan_id: str = Field(min_length=3, max_length=50)
    quantity: Optional[str] = Field(min_length=1, max_length=32)
    custom_id: Optional[str] = Field(min_length=1, max_length=127)
    status: Optional[str] = Field(min_length=1, max_length=24)
    status_change_note: Optional[str] = Field(min_length=1, max_length=128)
    status_update_time: Optional[str] = Field(min_length=20, max_length=64)
    # todo plan_overridden
    # todo start_time
    # todo shipping_amount
    # todo subscriber
    # todo application_context
    # todo plan
    # todo create_time
    # todo update_time

class SubscriptionReason(BaseModel):
    reason: str = Field(min_length=1, max_length=127) 