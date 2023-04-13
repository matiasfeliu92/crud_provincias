from django.test import TestCase
from django.urls.base import reverse

from .models import Provinces

# Create your tests here.
class ProvincesModelTests(TestCase):
    def test_get_one_province(self):
        """if not province exist with passed id, return appropiate message"""
        province = Provinces.objects.create(id=1, name='Santa Fe', population=23142323, density=5.8, surface=3252352)
        response = self.client.get(reverse('provinciasCrud:get_one_province', args=[province.id]))
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Santa Fe')
        # self.assertQuerysetEqual(response.context['province'], {})

    def test_get_all_provinces(self):
        """if provinces array is empty, return appropiate message"""
        province = Provinces.objects.create(id=1, name='Santa Fe', population=23142323, density=5.8, surface=3252352)
        response = self.client.get(reverse('provinciasCrud:get_provinces'))
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Santa Fe')