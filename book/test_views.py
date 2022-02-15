from django.test import TestCase

from services.models import Service, ServiceCategory


class TestBookViews(TestCase):
    """
    Test views in book app
    """
    def setUp(self):
        """
        Set up info needed for testing
        """

        self.servicecategory1 = ServiceCategory.objects.create(
            name='testServiceCategory',
            friendly_name='TestServiceCategory',
        )

        self.service1 = Service.objects.create(
            category=self.servicecategory1,
            name='testService',
            description='test',
            rating='5.0',
            image='test',
        )

        self.book_with_services = [{
            'service': str(self.service1.id),
            'total': 123
        }]

    def test_view_book_view(self):
        """
        Test that book is viewable
        """
        response = self.client.get('/book/')
        self.assertTrue(response.status_code, 200)

    def test_add_to_book_view(self):
        """
        Test that item can be added to book
        """
        book_data = {
            'service': Service.objects.get(pk=self.service1.id),
            'redirect_url': f'/services/{self.service1.id}/'
        }

        response = self.client.post(f'/book/add/{self.service1.id}/',
                                    book_data)
        self.assertEqual(response.status_code, 302)
