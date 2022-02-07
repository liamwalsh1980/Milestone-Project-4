from django.test import TestCase


class TestHomeViews(TestCase):
    """
    Test the home page views
    """
    def test_page_access(self):
        """
        Test home page is accessible
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
