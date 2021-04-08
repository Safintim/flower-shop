from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.serializers import ReasonSerializer
from main.models import Reason


class ReasonTests(APITestCase):
    def setUp(self):
        self.active_reason = Reason.objects.create(title='День рождение', is_active=True)
        self.not_active_reason = Reason.objects.create(title='8 марта')

    def test_list(self):
        url = reverse('api:reason-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.active_reason.title)

    def test_retrieve_active_reason(self):
        url = reverse('api:reason-detail', args=[self.active_reason.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, ReasonSerializer(self.active_reason).data)

    def test_retrieve_not_active_reason(self):
        url = reverse('api:category-detail', args=[self.not_active_reason.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
