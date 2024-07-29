from typing import Optional, Literal

from pydantic import BaseModel, Field

from paypal2.models.common import MonetaryValue, HATEOASLink


class Breakdown(BaseModel):
    item_total: Optional[MonetaryValue]
    shipping: Optional[MonetaryValue]
    handling: Optional[MonetaryValue]
    tax_total: Optional[MonetaryValue]
    insurance: Optional[MonetaryValue]
    shipping_discount: Optional[MonetaryValue]
    discount: Optional[MonetaryValue]


class MonetaryValueWithBreakdown(MonetaryValue):
    breakdown: Optional[Breakdown]


class Item(BaseModel):
    name: str = Field(min_length=1, max_length=127)
    quantity: str = Field(min_length=1, max_length=10)
    description: Optional[str] = Field(min_length=1, max_length=127)
    sku: Optional[str] = Field(min_length=1, max_length=127)
    url: Optional[str] = Field(min_length=1, max_length=2048)
    category: Optional[Literal["DIGITAL_GOODS", "PHYSICAL_GOODS", "DONATION"]] = Field(min_length=1, max_length=20)
    image_url: Optional[str] = Field(
        min_length=1, max_length=2048, pattern=r"^(https:)([/|.|\w|\s|-])*\.(?:jpg|gif|png|jpeg|JPG|GIF|PNG|JPEG)"
    )
    unit_amount: MonetaryValue  # purchase_units[].amount.breakdown.item_total must be set if present
    tax: Optional[MonetaryValue]  # purchase_units[].amount.breakdown.tax_total must be set if present
    # TODO: upc


class PurchaseUnit(BaseModel):
    reference_id: Optional[str] = Field(min_length=1, max_length=256)
    description: Optional[str] = Field(min_length=1, max_length=127)
    custom_id: Optional[str] = Field(min_length=1, max_length=256)
    invoice_id: Optional[str] = Field(min_length=1, max_length=256)
    soft_descriptor: Optional[str] = Field(min_length=1, max_length=22)
    items: Optional[list[Item]]


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
    intent: Optional[Literal["CAPTURE", "AUTHORIZE"]]
    # todo payer
    # todo purchase_units
    # todo create_time
    # todo update_time
