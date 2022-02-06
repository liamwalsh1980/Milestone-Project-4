from django.test import TestCase
from .forms import ProductForm


class TestProductForm(TestCase):
    """
    Test that the product form works
    """

    def test_name_is_required(self):
        """
        Test if form submits without name field
        """
        form = ProductForm({
            'name': '',
            'description': 'test',
            'price': 'test',
        })
        # Form should not be valid - name required
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['name'][0], 'This field is required.')

    def test_description_is_required(self):
        """
        Test if form submits without description field
        """
        form = ProductForm({
            'name': 'test',
            'description': '',
            'price': 'test',
        })
        # Form should not be valid - description required
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['description'][0], 'This field is required.')

    def test_price_is_required(self):
        """
        Test if form submits without price field
        """
        form = ProductForm({
            'name': 'test',
            'description': 'test',
            'price': '',
        })
        # Form should not be valid - price required
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['price'][0], 'This field is required.')
