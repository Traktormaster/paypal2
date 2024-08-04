import math
import random

import pytest

from paypal2.utility import simple_single_item_order_create


@pytest.mark.order(5)
def test_simple_single_item_order_create():
    for _ in range(1000):
        o = simple_single_item_order_create(
            "A",
            round(0.1 + 3000 * random.random(), 2),
            tax=round(0.1 + 500 * random.random(), 2) if random.random() > 0.5 else None,
            quantity=random.randint(1, 120),
        )
        unit_price = float(o.purchase_units[0].items[0].unit_amount.value)
        unit_quantity = int(o.purchase_units[0].items[0].quantity)
        total_price = float(o.purchase_units[0].amount.breakdown.item_total.value)
        assert math.isclose(unit_price * unit_quantity, total_price)
        all_total = total_price
        if o.purchase_units[0].items[0].tax:
            tax_price = float(o.purchase_units[0].items[0].tax.value)
            total_tax = float(o.purchase_units[0].amount.breakdown.tax_total.value)
            assert math.isclose(tax_price * unit_quantity, total_tax)
            all_total += total_tax
        assert math.isclose(float(o.purchase_units[0].amount.value), all_total)

    for _ in range(1000):
        o = simple_single_item_order_create(
            "A",
            random.randint(1, 1000000),
            tax=random.randint(1, 200000) if random.random() > 0.5 else None,
            quantity=random.randint(1, 120),
        )
        unit_price = int(o.purchase_units[0].items[0].unit_amount.value)
        unit_quantity = int(o.purchase_units[0].items[0].quantity)
        total_price = int(o.purchase_units[0].amount.breakdown.item_total.value)
        assert unit_price * unit_quantity == total_price
        all_total = total_price
        if o.purchase_units[0].items[0].tax:
            tax_price = int(o.purchase_units[0].items[0].tax.value)
            total_tax = int(o.purchase_units[0].amount.breakdown.tax_total.value)
            assert tax_price * unit_quantity == total_tax
            all_total += total_tax
        assert int(o.purchase_units[0].amount.value) == all_total
