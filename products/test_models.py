from django.test import TestCase

from .models import Category, Product


class TestProductModels(TestCase):
    """
    Test that the products work as expected
    """

    fixtures = [
        'categories.json',
        'products.json',
    ]

    def test_product_name(self):
        """
        Test that the product name is retrieved correctly
        """
        product = Product.objects.get(pk=1)
        self.assertEqual(product.name, 'Carrera Virtuoso Mens Road Bike')
        self.assertNotEqual(product.name, 'Test name')
        self.assertEqual(str(product), product.name)

    def test_product_description(self):
        """
        Test that the product description is retrieved correctly
        """
        product = Product.objects.get(pk=1)
        self.assertEqual(
            product.description, "Shimano Claris 2x8 (16 speed), Mechanical Disc Brakes with Alloy blades and Hi-tensile steel steerer"
        )
        self.assertNotEqual(product.description, 'test description incorrect')

    def test_product_has_sizes(self):
        """
        Test whether a product has sizes or not
        """
        product_sizes = Product.objects.get(pk=1)
        product_no_sizes = Product.objects.get(pk=43)
        self.assertEqual(product_sizes.has_sizes, False)
        self.assertNotEqual(product_sizes.has_sizes, True)
        self.assertNotEqual(product_no_sizes.has_sizes, True)
        self.assertEqual(product_no_sizes.has_sizes, False)


class TestCategoryModels(TestCase):
    """
    Test that the categories work as expected
    """

    fixtures = [
        'categories.json',
    ]

    def test_category_name(self):
        """
        Test that the category name is retrieved correctly
        """
        category = Category.objects.get(pk=1)
        self.assertEqual(category.name, 'mens_bikes')
        self.assertNotEqual(category.name, 'test')
        self.assertEqual(str(category), category.name)

    def test_category_friendly_name(self):
        """
        Test that the category friendly name is retrieved correctly
        """
        category = Category.objects.get(pk=3)
        self.assertEqual(category.friendly_name, 'Urban Bikes')
        self.assertNotEqual(category.friendly_name, 'Test Category')
        self.assertEqual(
            Category.get_friendly_name(category), category.friendly_name)
