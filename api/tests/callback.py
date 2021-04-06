from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.models import Callback


class CallbackTests(APITestCase):
    def test_create_valid(self):
        url = reverse('api:callback-list')
        data = {'phone': '89175468987'}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Callback.objects.filter(phone=data['phone']).exists())

    def test_create_not_valid(self):
        url = reverse('api:callback-list')
        data = {'phone': 'asdasdsad'}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

