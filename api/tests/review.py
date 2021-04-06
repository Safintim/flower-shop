from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from reviews.models import Review


class ReviewTests(APITestCase):
    def setUp(self):
        self.active_review = Review.objects.create(phone='89177654326', name='Lil', text='Thank you', is_active=True)
        self.not_active_review = Review.objects.create(phone='89177654326', name='Lil', text='I did not like')

    def test_list(self):
        url = reverse('api:review-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['name'], self.active_review.name)

    def test_retrieve(self):
        url = reverse('api:review-detail', args=[self.active_review.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_valid(self):
        url = reverse('api:review-list')
        data = {
            'phone': '89175468987',
            'name': 'Ivan',
            'social_link': 'https://vk.com/?id=213123123'
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Review.objects.filter(phone=data['phone'], name=data['name']).exists())

    def test_create_not_valid(self):
        url = reverse('api:review-list')
        data = {
            'phone': '89175468987',
            'social_link': 'not_valid'
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('name' in response.data)
        self.assertTrue('social_link' in response.data)

