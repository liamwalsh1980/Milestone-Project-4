from django.test import TestCase


class TestCompletetViews(TestCase):
    """
    Test that the complete works properly
    """

    def test_the_complete_page_url_exists(self):
        """
        Test that the complete page URL exists
        """
        response = self.client.get('/complete/')
        self.assertEqual(response.status_code, 200)
