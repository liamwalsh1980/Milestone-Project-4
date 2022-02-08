from django.test import TestCase

from services.models import Service
from .models import Booking


class TestBookingModels(TestCase):
    """
    Test that booking models work correctly
    """

    def setUp(self):
        Booking.objects.create(
            full_name='testname',
            email='test@test.com',
            phone_number='01234567890',
            more_information='testinfo',
            date='Feb. 8, 2022, 7:32 p.m.'
        )

    def test_booking_string_method_returns_booking_number(self):
        """
        Test string method for Booking class
        """
        booking_number = Booking.objects.create(booking_number='100')
        self.assertEqual(str(booking_number), '100')


class TestBookingLineItemModels(TestCase):
    """
    Test that the booking models work as expected
    """

    def test_booking_line_item_string_method(self):
        """
        Test that the string method works for the BookingineItem class
        """
        service = Service.objects.create()
        booking = Booking.objects.create(booking_number='100')
        expected_output = 'on booking 100'
        self.assertEqual(str(
            f'{service}on booking {booking.booking_number}'),
            expected_output)
