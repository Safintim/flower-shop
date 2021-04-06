from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.serializers import ColorSerializer
from main.models import Color


class ColorTests(APITestCase):
    def setUp(self):
        self.active_color = Color.objects.create(title='Нежный', is_active=True)
        self.not_active_color = Color.objects.create(title='Яркий')

    def test_list(self):
        url = reverse('api:color-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.active_color.title)

    def test_retrieve_active_color(self):
        url = reverse('api:color-detail', args=[self.active_color.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, ColorSerializer(self.active_color).data)

    def test_retrieve_no_active_color(self):
        url = reverse('api:color-detail', args=[self.not_active_color.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
