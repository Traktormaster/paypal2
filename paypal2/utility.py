from typing import Optional

from paypal2.models.common import MonetaryValue
from paypal2.models.order import OrdersCreate, PurchaseUnit, Item, MonetaryValueWithBreakdown, Breakdown


def format_monetary_value(v: float | int) -> str:
    if isinstance(v, float):
        return "%.2f" % v
    return str(v)


def simple_single_item_order_create(
    item_id: str,
    item_name: str,
    price: float | int,
    currency_code: str = "USD",
    tax: Optional[float | int] = None,
    quantity: int = 1,
    category: str = "DIGITAL_GOODS",
    intent: str = "CAPTURE",
) -> OrdersCreate:
    assert quantity > 0
    unit_amount = MonetaryValue(currency_code=currency_code, value=format_monetary_value(price))
    total_price = price * quantity
    item_total = MonetaryValue(currency_code=currency_code, value=format_monetary_value(total_price))
    total = total_price
    if tax is None:
        tax_total = unit_tax = None
    else:
        unit_tax = MonetaryValue(currency_code=currency_code, value=format_monetary_value(tax))
        total_tax = tax * quantity
        tax_total = MonetaryValue(currency_code=currency_code, value=format_monetary_value(total_tax))
        total += total_tax
    return OrdersCreate(
        purchase_units=[
            PurchaseUnit(
                items=[
                    Item(
                        id=item_id,
                        name=item_name,
                        quantity=str(quantity),
                        category=category,
                        unit_amount=unit_amount,
                        tax=unit_tax,
                    ),
                ],
                amount=MonetaryValueWithBreakdown(
                    currency_code=currency_code,
                    value=format_monetary_value(total),
                    breakdown=Breakdown(
                        item_total=item_total,
                        tax_total=tax_total,
                    ),
                ),
            )
        ],
        intent=intent,
    )
