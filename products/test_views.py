from django.test import TestCase


from django.shortcuts import get_object_or_404
from django.contrib.messages import get_messages

from profiles.models import User
from .models import Product, Category
from .forms import ProductForm


class TestProductsViews(TestCase):
    """
    Test views in products app
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
            has_sizes='True',
            price='100',
            rating='5.5',
            image='test'
        )

        self.admin_user = User.objects.create_superuser(
            username='admin',
            password='adminpassword',
            email='admintest@test.com',
        )

        self.user = User.objects.create_user(
            username='user',
            password='password',
            email='test@test.com',
        )

    def test_all_products_view(self):
        """
        Test that all users can view all products page
        """
        response = self.client.get('/products/')
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_view(self):
        """
        Test that all users can view product details page
        """
        response = self.client.get(f'/products/{self.product1.id}/')
        self.assertTemplateUsed(response, 'products/product_detail.html')
        self.assertEqual(response.status_code, 200)

    def test_add_product_view(self):
        """
        Test that only admin can access add_product page
        """

        # Check page loads if user is admin
        self.client.force_login(self.admin_user)
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        # Check page redirects if non-admin logged in
        self.client.force_login(self.user)
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 302)
        self.client.logout()

        # Check page redirects if user not logged in
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 302)

    def test_edit_product_view(self):
        """
        Test that only admin can access edit_product page.
        """

        # Check page loads if user is admin
        self.client.force_login(self.admin_user)
        response = self.client.get(f'/products/edit/{self.product1.id}/')
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        # Check page redirects if non-admin logged in
        self.client.force_login(self.user)
        response = self.client.get(f'/products/edit/{self.product1.id}/')
        self.assertEqual(response.status_code, 302)
        self.client.logout()

        # Check page redirects if user not logged in
        response = self.client.get(f'/products/edit/{self.product1.id}/')
        self.assertEqual(response.status_code, 302)

    def test_edit_product(self):
        """
        Test that admin can edit products
        """
        self.client.force_login(self.admin_user)
        product = get_object_or_404(Product, pk=self.product1.id)
        product_form = ProductForm({
            'category': self.category1.pk,
            'name': 'testEditProduct',
            'description': 'testEditDescription',
            'has_sizes': 'False',
            'price': '101',
            'rating': '4.0',
            'image': 'testEditImage'
        },
            instance=product
        )
        self.assertTrue(product_form.is_valid())
        product_form.save()
        self.client.post(f'/products/edit/{self.product1.id}/')
        updated_product = Product.objects.get(id=self.product1.id)
        self.assertEqual(updated_product.name, 'testEditProduct')

    def test_delete_product_works_for_admin(self):
        """
        Test that admin can delete products
        """
        self.client.force_login(self.admin_user)
        response = self.client.get(f'/products/delete/{self.product1.id}/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(messages[0].tags, 'success')
        self.assertEqual(
            str(messages[0]), 'Product deleted!')
        self.assertEqual(response.status_code, 302)
        self.client.logout()

    def test_delete_product_doesnt_work_for_non_admin(self):
        """
        Test that non-admins cannot delete products
        """
        self.client.force_login(self.user)
        response = self.client.get(f'/products/delete/{self.product1.id}/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(messages[0].tags, 'error')
        self.assertEqual(
            str(messages[0]), 'Sorry, only store owners can do that.')
        self.assertEqual(response.status_code, 302)
        self.client.logout()
