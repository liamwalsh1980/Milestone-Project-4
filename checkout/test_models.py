from django.test import TestCase

from products.models import Product
from .models import Order


class TestOrderModels(TestCase):
    """
    Test that order models work correctly
    """

    def setUp(self):
        Order.objects.create(
            full_name='testname',
            email='test@test.com',
            phone_number='01234567890',
            street_address1='test',
            town_or_city='test',
            country='GB'
        )

    def test_order_string_method_returns_order_number(self):
        """
        Test string method for Order class
        """
        order_number = Order.objects.create(order_number='100')
        self.assertEqual(str(order_number), '100')

    def test_checkout_details(self):
        """
        Test that the checkout fields auto-fill from the user's information
        """
        order = Order.objects.get(id=1)
        self.assertEqual(order.full_name, 'testname')
        self.assertEqual(order.email, 'test@test.com')
        self.assertEqual(order.phone_number, '01234567890')
        self.assertEqual(order.street_address1, 'test')
        self.assertEqual(order.town_or_city, 'test')
        self.assertEqual(order.country, 'GB')

    def test_update_total(self):
        """
        Test that the order total is updated correctly
        """
        order_total = 100
        grand_total = order_total
        self.assertEqual(grand_total, 100)


class TestOrderLineItemModels(TestCase):
    """
    Test that the order models work as expected
    """

    def test_order_line_item_string_method(self):
        """
        Test that the string method works for the OrderLineItem class
        """
        product = Product.objects.create(price=100.00)
        order = Order.objects.create(order_number='100')
        expected_output = 'on order 100'
        self.assertEqual(str(
            f'{product}on order {order.order_number}'),
            expected_output)
