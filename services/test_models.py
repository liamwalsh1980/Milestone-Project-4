from django.test import TestCase

from .models import Service, ServiceCategory


class TestServiceModels(TestCase):
    """
    Test that the products work as expected
    """

    fixtures = [
        'servicecategories.json',
        'services.json',
    ]

    def test_service_name(self):
        """
        Test that the service name is retrieved correctly
        """
        service = Service.objects.get(pk=3)
        self.assertEqual(service.name, 'Sell your bike service')
        self.assertNotEqual(service.name, 'Test name')
        self.assertEqual(str(service), service.name)

    def test_service_description(self):
        """
        Test that the service description is retrieved correctly
        """
        service = Service.objects.get(pk=3)
        self.assertEqual(
            service.description, "Sell your bike and put what its worth towards a new one. Book a date and time thats suitable to bring your bike in for a free appraisal"
        )
        self.assertNotEqual(service.description, 'test description incorrect')


class TestServiceCategoryModels(TestCase):
    """
    Test that the service categories work as expected
    """

    fixtures = [
        'servicecategories.json',
    ]

    def test_servicecategory_name(self):
        """
        Test that the service category name is retrieved correctly
        """
        servicecategory = ServiceCategory.objects.get(pk=1)
        self.assertEqual(servicecategory.name, 'bike_services')
        self.assertNotEqual(servicecategory.name, 'test')
        self.assertEqual(str(servicecategory), servicecategory.name)

    def test_servicecategory_friendly_name(self):
        """
        Test that the category friendly name is retrieved correctly
        """
        servicecategory = ServiceCategory.objects.get(pk=1)
        self.assertEqual(servicecategory.friendly_name, 'Bike Services')
        self.assertNotEqual(servicecategory.friendly_name, 'Test Service Category')
        self.assertEqual(
            ServiceCategory.get_friendly_name(servicecategory), servicecategory.friendly_name)
