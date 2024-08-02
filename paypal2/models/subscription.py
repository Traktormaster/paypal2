from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from paypal2.models.common import HATEOASLink


class SubscriptionCreate(BaseModel):
    id: str = Field(min_length=26, max_length=26)
    quantity: Optional[str] = Field(min_length=1, max_length=32, default=None)
    custom_id: Optional[str] = Field(min_length=1, max_length=127, default=None)  # can be invoice id
    start_time: Optional[datetime] = None
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
    quantity: Optional[str] = Field(min_length=1, max_length=32, default=None)
    custom_id: Optional[str] = Field(min_length=1, max_length=127, default=None)
    status: Optional[str] = Field(min_length=1, max_length=24, default=None)
    status_change_note: Optional[str] = Field(min_length=1, max_length=128, default=None)
    status_update_time: Optional[str] = Field(min_length=20, max_length=64, default=None)
    plan_overridden: Optional[bool] = None
    start_time: Optional[datetime] = None
    create_time: Optional[datetime] = None
    update_time: Optional[datetime] = None
    # todo shipping_amount
    # todo subscriber
    # todo application_context
    # todo plan


class SubscriptionReason(BaseModel):
    reason: str = Field(min_length=1, max_length=127)


class SubscriptionTransaction(BaseModel):
    id: str
    status: str
    time: str


class SubscriptionTransactionList(BaseModel):
    transactions: list[SubscriptionTransaction]
    total_items: Optional[int] = None
    total_pages: Optional[int] = None
    # todo links
