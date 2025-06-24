from decimal import Decimal

import pytest
from django.utils import timezone

from cart.models import Cart, CartItem
from products.models import Product


@pytest.mark.django_db
class TestCartModels:

    def test_cart_item_total_price(self):
        product = Product.objects.create(name="Laptop", price=Decimal("1000.00"))
        cart = Cart.objects.create()
        item = CartItem.objects.create(cart=cart, product=product, quantity=3)

        assert item.get_total_price() == Decimal("3000.00")

    def test_cart_total_price_multiple_items(self):
        product1 = Product.objects.create(name="Mouse", price=Decimal("50.00"))
        product2 = Product.objects.create(name="Keyboard", price=Decimal("150.00"))
        cart = Cart.objects.create()
        CartItem.objects.create(cart=cart, product=product1, quantity=2)
        CartItem.objects.create(cart=cart, product=product2, quantity=1)

        total = cart.get_total_price()
        assert total == Decimal("250.00")
