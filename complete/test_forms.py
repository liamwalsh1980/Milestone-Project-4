from django.test import TestCase
from .forms import BookingForm


class TestBookingForm(TestCase):
    """
    Test that the booking form works with required fields
    """

    def test_full_name_is_required(self):
        """
        Test if form submits without full_name field completed
        """
        form = BookingForm({
            'full_name': '',
            'email': 'test@test.com',
            'phone_number': '01234567890',
            'more_information': '',
        })
        # Form should not be valid, as full_name is required field
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        # Check that the error message is correct
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.')

    def test_email_is_required(self):
        """
        Test if form submits without email field completed
        """
        form = BookingForm({
            'full_name': 'testname',
            'email': '',
            'phone_number': '01234567890',
            'more_information': '',
        })
        # Form should not be valid, as email is required field
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(
            form.errors['email'][0], 'This field is required.')

    def test_phone_number_is_required(self):
        """
        Test if form submits without phone_number field completed
        """
        form = BookingForm({
            'full_name': 'testname',
            'email': 'test@test.com',
            'phone_number': '',
            'more_information': '',
        })
        # Form should not be valid, as phone_number is required field
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Check that the form fields that are visible
        to the user are the correct ones
        """
        form = BookingForm()
        self.assertEqual(form.Meta.fields, (
            'full_name', 'email', 'phone_number', 'more_information',
        ))
