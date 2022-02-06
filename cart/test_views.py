from django.test import TestCase

from products.models import Product, Category


class TestCartViews(TestCase):
    """
    Test views in cart app
    """
    def setUp(self):
        """
        Set up info needed for testing
        """

        self.category1 = Category.objects.create(
            name='testCategory',
            friendly_name='TestCategory',
        )

        self.product1 = Product.objects.create(
            category=self.category1,
            name='testProduct',
            description='test',
            price='100',
            image='test',
        )

        self.quantity = 1

        self.bag_with_products = [{
            'product': str(self.product1.id),
            'quantity': int(self.quantity),
            'total': 123
        }]

    def test_view_cart_view(self):
        """
        Test that cart is viewable
        """
        response = self.client.get('/cart/')
        self.assertTrue(response.status_code, 200)

    def test_add_to_cart_view(self):
        """
        Test that item can be added to cart
        """
        cart_data = {
            'product': Product.objects.get(pk=self.product1.id),
            'quantity': int(self.quantity),
            'redirect_url': f'/products/{self.product1.id}/'
        }

        response = self.client.post(f'/cart/add/{self.product1.id}/', cart_data)
        self.assertEqual(response.status_code, 302)
