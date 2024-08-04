from datetime import datetime
from typing import Optional, Literal

from pydantic import BaseModel, Field

from paypal2.models.common import MonetaryValue, HATEOASLink


class Breakdown(BaseModel):
    item_total: Optional[MonetaryValue] = None
    shipping: Optional[MonetaryValue] = None
    handling: Optional[MonetaryValue] = None
    tax_total: Optional[MonetaryValue] = None
    insurance: Optional[MonetaryValue] = None
    shipping_discount: Optional[MonetaryValue] = None
    discount: Optional[MonetaryValue] = None


class MonetaryValueWithBreakdown(MonetaryValue):
    breakdown: Optional[Breakdown] = None


class Item(BaseModel):
    name: str = Field(min_length=1, max_length=127)
    quantity: str = Field(min_length=1, max_length=10)
    description: Optional[str] = Field(min_length=1, max_length=127, default=None)
    sku: Optional[str] = Field(min_length=1, max_length=127, default=None)
    url: Optional[str] = Field(min_length=1, max_length=2048, default=None)
    category: Optional[Literal["DIGITAL_GOODS", "PHYSICAL_GOODS", "DONATION"]] = Field(
        min_length=1, max_length=20, default=None
    )
    image_url: Optional[str] = Field(
        min_length=1,
        max_length=2048,
        pattern=r"^(https:)([/|.|\w|\s|-])*\.(?:jpg|gif|png|jpeg|JPG|GIF|PNG|JPEG)",
        default=None,
    )
    unit_amount: MonetaryValue  # purchase_units[].amount.breakdown.item_total must be set if present
    tax: Optional[MonetaryValue] = None  # purchase_units[].amount.breakdown.tax_total must be set if present
    # TODO: upc


class PurchaseUnit(BaseModel):
    reference_id: Optional[str] = Field(min_length=1, max_length=256, default=None)
    description: Optional[str] = Field(min_length=1, max_length=127, default=None)
    custom_id: Optional[str] = Field(min_length=1, max_length=255, default=None)
    invoice_id: Optional[str] = Field(min_length=1, max_length=127, default=None)
    soft_descriptor: Optional[str] = Field(min_length=1, max_length=22, default=None)
    items: Optional[list[Item]] = None
    amount: MonetaryValueWithBreakdown
    # TODO: payee
    # TODO: payment_instruction
    # TODO: shipping
    # TODO: supplementary_data


class OrdersCreate(BaseModel):
    purchase_units: list[PurchaseUnit] = Field(min_length=1, max_length=10)
    intent: Optional[Literal["CAPTURE", "AUTHORIZE"]]
    # TODO: payment_source


class OrderMinimalResponse(BaseModel):
    id: str
    status: str
    links: list[HATEOASLink]


class OrderCreated(OrderMinimalResponse):
    processing_instruction: Optional[Literal["ORDER_COMPLETE_ON_PAYMENT_APPROVAL", "NO_INSTRUCTION"]] = Field(
        min_length=1, max_length=36, pattern=r"^[0-9A-Z_]+$", default="NO_INSTRUCTION"
    )
    intent: Optional[Literal["CAPTURE", "AUTHORIZE"]] = None
    create_time: Optional[datetime] = None
    update_time: Optional[datetime] = None
    # todo payer
    # todo purchase_units
