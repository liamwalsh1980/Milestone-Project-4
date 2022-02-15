from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.messages import get_messages

from .models import UserProfile


class TestProfilesViews(TestCase):
    """
    Test profiles page views
    """
    def setUp(self):
        """
        Set up info needed for testing
        """

        self.test_user = User.objects.create_user(
            username='testname',
            email='test@test.com',
            password='password',
        )

        self.test_user_profile = get_object_or_404(UserProfile,
                                                   user=self.test_user)

    def test_profile_view(self):
        """
        Test that user can access profile page when logged in
        """

        # Check page loads if user logged in
        self.client.force_login(self.test_user)
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('profiles/profile.html')
        self.client.logout()

        # # Check page redirects if user not logged in
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('accounts/login/')

    def test_default_delivery_information_updates(self):
        """
        Test that default delivery info updates
        """
        self.client.force_login(self.test_user)
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('profiles/profile.html')

        new_data = {
            'default_phone_number': 'testEdit',
            'default_street_address1': 'testEdit',
            'default_street_address2': 'testEdit',
            'default_town_or_city': 'testEdit',
            'default_county': 'testEdit',
            'default_postcode': 'testEdit',
            'default_country': 'GB'
        }
        self.client.post('/profile/', new_data)
        response = self.client.post('/profile/', new_data)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'success')
        self.assertEqual(
            str(messages[0]), 'Profile updated successfully')
        self.client.logout()
