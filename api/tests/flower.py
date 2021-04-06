from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.serializers import FlowerSerializer
from main.models import Flower


class FlowerTests(APITestCase):
    def setUp(self):
        self.active_flower = Flower.objects.create(title='Лилия', price=100, is_active=True)
        self.not_active_flower = Flower.objects.create(title='Пион', price=80)

    def test_list(self):
        url = reverse('api:flower-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.active_flower.title)

    def test_retrieve_active_reason(self):
        url = reverse('api:flower-detail', args=[self.active_flower.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, FlowerSerializer(self.active_flower).data)

    def test_retrieve_not_active_category(self):
        url = reverse('api:flower-detail', args=[self.not_active_flower.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
