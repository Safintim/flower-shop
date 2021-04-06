from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.serializers import CartSerializer
from cart.models import Cart

User = get_user_model()


class CartTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(phone='89177654326')

    def test_not_auth(self):
        url = reverse('api:cart-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_not_exists_cart(self):
        url = reverse('api:cart-list')
        self.client.force_login(user=self.user)
        response = self.client.get(url)
        carts = Cart.objects.filter(user=self.user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(carts.exists())
        self.assertEqual(response.data, CartSerializer(carts.first()).data)

    def test_list_exists_cart(self):
        cart = Cart.objects.create(user=self.user)
        self.client.force_login(user=self.user)

        url = reverse('api:cart-list')
        response = self.client.get(url)
        carts = Cart.objects.filter(user=self.user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(carts.count(), 1)
        self.assertEqual(response.data, CartSerializer(cart).data)

    def test_retrieve(self):
        cart = Cart.objects.create(user=self.user)
        url = reverse('api:cart-detail', args=[cart.pk])
        self.client.force_login(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_add_to_cart(self):
        pass

    def test_delete_from_cart(self):
        pass
