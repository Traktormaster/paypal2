from paypal2.models.common import MonetaryValue
from paypal2.models.order import OrdersCreate, PurchaseUnit, Item, MonetaryValueWithBreakdown, Breakdown


def simple_single_order_create(
    item_id: str,
    item_name: str,
    price: float | int | str,
    currency_code: str = "USD",
    category: str = "DIGITAL_GOODS",
    intent: str = "CAPTURE",
) -> OrdersCreate:
    return OrdersCreate(
        purchase_units=[
            PurchaseUnit(
                items=[
                    Item(
                        id=item_id,
                        name=item_name,
                        quantity="1",
                        category=category,
                        unit_amount=MonetaryValue(
                            currency_code=currency_code,
                            value=str(price),
                        ),
                    ),
                ],
                amount=MonetaryValueWithBreakdown(
                    currency_code=currency_code,
                    value=str(price),
                    breakdown=Breakdown(
                        item_total=MonetaryValue(
                            currency_code=currency_code,
                            value=str(price),
                        ),
                    ),
                ),
            )
        ],
        intent=intent,
    )
