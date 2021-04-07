from datetime import datetime

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.serializers import OrderSerializer, OrderCreateSerializer
from cart.models import Cart, CartProduct
from main.models import Product
from orders.models import Order

User = get_user_model()


class OrderTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(phone='89177654326')

    def test_not_auth(self):
        url = reverse('api:order-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list(self):
        self.client.force_login(user=self.user)
        Order.objects.create(user=self.user, delivery_date=datetime.now())

        url = reverse('api:order-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, OrderSerializer(Order.objects.filter(user=self.user), many=True).data)

    def create_order(self):
        url = reverse('api:order-list')
        data = {
            'delivery_date': datetime.now().strftime('%Y-%m-%d'),
            'delivery_time': datetime.now().strftime('%H:%M')
        }
        response = self.client.post(url, data=data)
        return response

    def test_create_order_with_empty_cart(self):
        self.client.force_login(user=self.user)
        response = self.create_order()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_order_with_not_empty_cart(self):
        self.client.force_login(user=self.user)
        cart = Cart.objects.create(user=self.user)
        product = Product.objects.create(type=Product.Type.PRESENT, is_active=True, title='Конфеты', price=600)
        cart.add_product(product)
        response = self.create_order()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        order = Order.objects.filter(user=self.user).first()
        self.assertEqual(response.data, OrderCreateSerializer(order).data)
        self.assertEqual(Order.objects.filter(user=self.user).count(), 1)
        self.assertEqual(CartProduct.objects.filter(cart__user=self.user).count(), 0)
