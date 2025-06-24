from decimal import Decimal

import pytest
from django.urls import reverse

from products.models import Category, Product


@pytest.mark.django_db
class TestProductModels:

    def test_category_str(self):
        category = Category.objects.create(name="Laptops", slug="laptops")
        assert str(category) == "Laptops"

    def test_product_str(self):
        category = Category.objects.create(name="Monitores", slug="monitores")
        product = Product.objects.create(
            name="Monitor LG 27",
            slug="monitor-lg-27",
            category=category,
            stock=10,
            price=Decimal("800.00"),
            description="Monitor ultra ancho",
            available=True,
        )
        assert str(product) == "Monitor LG 27"

    def test_product_get_absolute_url(self):
        category = Category.objects.create(name="Teclados", slug="teclados")
        product = Product.objects.create(
            name="Teclado mecánico",
            slug="teclado-mecanico",
            category=category,
            stock=5,
            price=Decimal("150.00"),
            available=True,
        )

        expected_url = reverse(
            "products:product_detail", kwargs={"id": product.id, "slug": product.slug}
        )
        assert product.get_absolute_url() == expected_url
