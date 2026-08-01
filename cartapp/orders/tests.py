from django.test import TestCase
from django.urls import reverse


class CartPageTests(TestCase):
    def test_cart_page_renders_cart_shell(self):
        response = self.client.get(reverse("cart"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "cart-page-shell")

    def test_cart_page_renders_full_store_layout(self):
        response = self.client.get(reverse("cart"))

        self.assertContains(response, "THREAD")
        self.assertContains(response, "CRAFT")
        self.assertContains(response, "Shopping Cart")
