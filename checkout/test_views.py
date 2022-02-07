from django.test import TestCase

from django.contrib.messages import get_messages
from django.contrib.auth.models import User


class TestCheckoutViews(TestCase):
    """
    Test that the checkout works properly
    """

    def test_signin(self):
        """
        Test the signin page view
        """

        # test user cannot access page if logged in
        self.reg_user = User.objects.create_user(
            username='admin',
            password='password',
            email='testadmin@test.com',
            )
        self.client.force_login(self.reg_user)
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        # test user can access is not logged in
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_the_checkout_page_url_exists(self):
        """
        Test that the checkout page URL exists
        """
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 302)

    def test_nothing_in_cart_error(self):
        """
        Test that an error message is shown when nothing is in the shopping bag
        """
        response = self.client.get('/checkout/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'error')
        self.assertEqual(
            str(messages[0]), "There's nothing in your cart at the moment")
