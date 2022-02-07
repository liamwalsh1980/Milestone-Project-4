from django.test import TestCase


from .models import Service, ServiceCategory


class TestServicesViews(TestCase):
    """
    Test views in services app
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
            image='test'
        )

    def test_all_services_view(self):
        """
        Test that users can view all services page
        """
        response = self.client.get('/services/')
        self.assertTemplateUsed(response, 'services/services.html')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_view(self):
        """
        Test that users can view product details page
        """
        response = self.client.get(f'/services/{self.service1.id}/')
        self.assertTemplateUsed(response, 'services/service_detail.html')
        self.assertEqual(response.status_code, 200)
