from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.serializers import CartSerializer
from cart.models import Cart
from main.models import Product, Bouquet, Flower, BouquetFlower

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

    def check_add_to_cart(self, response):
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        cart = self.user.cart_set.first()
        self.assertEqual(response.data, CartSerializer(cart).data)
        self.assertEqual(cart.products.count(), 1)

    def test_add_present_to_cart_valid(self):
        self.client.force_login(user=self.user)
        present = Product.objects.create(type=Product.Type.PRESENT, title='Конфеты', price=600, is_active=True)
        data = {'product_id': present.pk}
        url = reverse('api:cart-add-present')
        response = self.client.post(url, data=data)
        self.check_add_to_cart(response)

    def test_add_bouquet_to_cart_valid(self):
        self.client.force_login(user=self.user)
        product = Product.objects.create(type=Product.Type.BOUQUET, title='Букет из пион', is_active=True)
        flower = Flower.objects.create(title='Пион', price=80)
        bouquet = Bouquet.objects.create(size=Bouquet.Size.MD)
        BouquetFlower.objects.create(count=10, flower=flower, bouquet=bouquet)
        product.bouquets.add(bouquet)

        data = {'product_id': product.pk, 'bouquet_size': bouquet.size}
        url = reverse('api:cart-add-bouquet')
        response = self.client.post(url, data=data)
        self.check_add_to_cart(response)

    def test_add_present_to_cart_not_valid(self):
        self.client.force_login(user=self.user)
        data = {'product_id': 123}
        url = reverse('api:cart-add-present')
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('product_id' in response.data)

    def test_add_bouquet_to_cart_not_valid(self):
        self.client.force_login(user=self.user)
        product = Product.objects.create(type=Product.Type.BOUQUET, title='Букет из пион', is_active=True)
        data = {'product_id': product.pk, 'bouquet_size': 'MIDDLE'}
        url = reverse('api:cart-add-bouquet')
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('bouquet_size' in response.data)

    def test_delete_from_cart_valid(self):
        self.client.force_login(user=self.user)
        product = Product.objects.create(type=Product.Type.PRESENT, title='Конфеты', price=600, is_active=True)
        cart = Cart.objects.create(user=self.user)
        cart.add_product(product)
        data = {'product_id': product.pk}
        url = reverse('api:cart-delete-product')
        response = self.client.delete(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(cart.products.count(), 0)

    def test_delete_from_cart_not_valid(self):
        self.client.force_login(user=self.user)
        data = {'product_id': 123}
        url = reverse('api:cart-delete-product')
        response = self.client.delete(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('product_id' in response.data)

