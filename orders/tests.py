from decimal import Decimal

import pytest

from orders.models import Order, OrderItem
from products.models import Category, Product


@pytest.mark.django_db
class TestOrderModels:

    def test_order_item_get_cost(self):
        category = Category.objects.create(name="Tablets", slug="tablets")
        product = Product.objects.create(
            name="iPad Mini",
            slug="ipad-mini",
            category=category,
            stock=20,
            price=Decimal("1200.00"),
            available=True,
        )
        order = Order.objects.create(
            full_name="Juan Pérez",
            email="juan@example.com",
            address="Calle 123",
            paid=True,
        )
        item = OrderItem.objects.create(
            order=order,
            product=product,
            price=product.price,
            quantity=2,
        )

        assert item.get_cost() == Decimal("2400.00")

    def test_order_get_total_cost(self):
        category = Category.objects.create(name="Gaming", slug="gaming")
        product1 = Product.objects.create(
            name="PS5",
            slug="ps5",
            category=category,
            stock=5,
            price=Decimal("3500.00"),
            available=True,
        )
        product2 = Product.objects.create(
            name="Xbox Series X",
            slug="xbox",
            category=category,
            stock=3,
            price=Decimal("3300.00"),
            available=True,
        )

        order = Order.objects.create(
            full_name="Ana Torres",
            email="ana@example.com",
            address="Carrera 45",
            paid=False,
        )

        OrderItem.objects.create(
            order=order, product=product1, price=product1.price, quantity=1
        )
        OrderItem.objects.create(
            order=order, product=product2, price=product2.price, quantity=2
        )

        total = order.get_total_cost()
        assert total == Decimal("10100.00")
