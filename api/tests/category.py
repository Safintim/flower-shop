from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.serializers import CategorySerializer
from main.models import Category


class CategoryTests(APITestCase):
    def setUp(self):
        self.active_category = Category.objects.create(title='Розы', is_active=True)
        self.not_active_category = Category.objects.create(title='Акции')

        self.parent_category = Category.objects.create(title='Цветы', is_active=True)
        self.children_category1 = Category.objects.create(title='Лилия', is_active=True, parent=self.parent_category)
        self.children_category2 = Category.objects.create(title='Пионы', is_active=True, parent=self.parent_category)

    def test_list(self):
        url = reverse('api:category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], self.active_category.title)

    def test_retrieve_active_category(self):
        url = reverse('api:category-detail', args=[self.active_category.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, CategorySerializer(self.active_category).data)

    def test_retrieve_not_active_category(self):
        url = reverse('api:category-detail', args=[self.not_active_category.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_list_only_parents(self):
        url = reverse('api:category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        categories = Category.objects.active().filter(parent=None)
        self.assertEqual(response.data, CategorySerializer(categories, many=True).data)
