from django.urls import reverse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from api.serializers import ProductSerializer
from main.models import Product, Flower, BouquetFlower, Bouquet, Category, Color, Reason


class ProductTests(APITestCase):

    def setUp(self):
        self.present1 = Product.objects.create(type=Product.Type.PRESENT, title='Конфеты1', price=600, is_active=True)
        self.present2 = Product.objects.create(type=Product.Type.PRESENT, title='Конфеты2', price=500, is_active=True)
        self.present3 = Product.objects.create(type=Product.Type.PRESENT, title='Конфеты3', price=1000, is_active=True)
        self.flower1 = Flower.objects.create(title='Пион', price=80, is_active=True, is_add_filter=True)
        self.flower2 = Flower.objects.create(title='Лилия', price=100, is_active=True, is_add_filter=True)
        self.flower3 = Flower.objects.create(title='Одуванчик', price=50, is_active=True, is_add_filter=True)

        self.bouquet1 = Bouquet.objects.create(size=Bouquet.Size.MD)
        self.bouquet2 = Bouquet.objects.create(size=Bouquet.Size.MD)
        self.bouquet3 = Bouquet.objects.create(size=Bouquet.Size.MD)

        BouquetFlower.objects.create(count=1, flower=self.flower1, bouquet=self.bouquet1)
        BouquetFlower.objects.create(count=3, flower=self.flower2, bouquet=self.bouquet1)
        BouquetFlower.objects.create(count=5, flower=self.flower3, bouquet=self.bouquet1)

        BouquetFlower.objects.create(count=3, flower=self.flower1, bouquet=self.bouquet2)
        BouquetFlower.objects.create(count=5, flower=self.flower2, bouquet=self.bouquet2)
        BouquetFlower.objects.create(count=7, flower=self.flower3, bouquet=self.bouquet2)

        BouquetFlower.objects.create(count=5, flower=self.flower1, bouquet=self.bouquet3)
        BouquetFlower.objects.create(count=7, flower=self.flower2, bouquet=self.bouquet3)
        BouquetFlower.objects.create(count=9, flower=self.flower3, bouquet=self.bouquet3)

        self.bouquet1.price = Bouquet.calculate_bouquet_price(self.bouquet1)
        self.bouquet2.price = Bouquet.calculate_bouquet_price(self.bouquet2)
        self.bouquet3.price = Bouquet.calculate_bouquet_price(self.bouquet3)

        self.bouquet1.save()
        self.bouquet2.save()
        self.bouquet3.save()

        self.bouquet_product1 = Product.objects.create(
            type=Product.Type.BOUQUET,
            title='Букет из Пион',
            is_active=True,
            price=self.bouquet1.price
        )
        self.bouquet_product1.bouquets.add(self.bouquet1)

        self.bouquet_product2 = Product.objects.create(
            type=Product.Type.BOUQUET,
            title='Букет из Лилий',
            is_active=True,
            price=self.bouquet2.price
        )
        self.bouquet_product2.bouquets.add(self.bouquet2)

        self.bouquet_product3 = Product.objects.create(
            type=Product.Type.BOUQUET,
            title='Букет из Одуванчиков',
            is_active=True,
            price=self.bouquet3.price
        )
        self.bouquet_product1.bouquets.add(self.bouquet3)

        self.category1 = Category.objects.create(title='8 марта', is_active=True)
        self.category2 = Category.objects.create(title='Подарки', is_active=True)
        self.category3 = Category.objects.create(title='Пионы', is_active=True)

        self.present1.categories.add(self.category2)
        self.present2.categories.add(self.category2)
        self.present3.categories.add(self.category2)
        self.bouquet_product1.categories.add(self.category1)
        self.bouquet_product2.categories.add(self.category1, self.category3)
        self.bouquet_product3.categories.add(self.category3)

        self.reason1 = Reason.objects.create(title='День рождение', is_active=True)
        self.reason2 = Reason.objects.create(title='Свадьба', is_active=True)
        self.reason3 = Reason.objects.create(title='Юбилей', is_active=True)

        self.present1.reasons.add(self.reason1)
        self.present2.reasons.add(self.reason3)
        self.bouquet_product1.reasons.add(self.reason2)
        self.bouquet_product2.reasons.add(self.reason2, self.reason3)
        self.bouquet_product3.reasons.add(self.reason2)

        self.color1 = Color.objects.create(title='Нежный')
        self.color2 = Color.objects.create(title='Яркий')

        self.bouquet_product1.color = self.color1
        self.bouquet_product2.color = self.color1
        self.bouquet_product3.color = self.color2
        self.bouquet_product1.save()
        self.bouquet_product2.save()
        self.bouquet_product3.save()

    def get_context(self, url):
        factory = APIRequestFactory()
        request = factory.get(url)
        return {'request': Request(request)}

    def test_list(self):
        url = reverse('api:product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['results'],
            ProductSerializer(Product.objects.active(), many=True, context=self.get_context(url)).data
        )
        self.assertEqual(response.data['count'], 6)

    def test_filter_by_category(self):
        url = reverse('api:product-list')
        data = {'categories': f'{self.category1.pk},{self.category2.pk}'}
        response = self.client.get(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        qs = Product.objects.active().filter(categories__in=[self.category1.pk, self.category2.pk])
        self.assertEqual(
            response.data['results'],
            ProductSerializer(qs, many=True, context=self.get_context(url)).data
        )

    def test_filter_by_color(self):
        url = reverse('api:product-list')
        data = {'color': self.color1.pk}
        response = self.client.get(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        qs = Product.objects.active().filter(color=self.color1.pk)
        self.assertEqual(
            response.data['results'],
            ProductSerializer(qs, many=True, context=self.get_context(url)).data
        )

    def test_filter_by_reason(self):
        url = reverse('api:product-list')
        data = {'reasons': f'{self.reason1.pk},{self.reason2.pk}'}
        response = self.client.get(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        qs = Product.objects.active().filter(reasons__in=[self.reason1.pk, self.reason2.pk])
        self.assertEqual(
            response.data['results'],
            ProductSerializer(qs, many=True, context=self.get_context(url)).data
        )

    def test_filter_by_price(self):
        url = reverse('api:product-list')
        data = {'price_min': self.bouquet_product1.price, 'price_max': self.bouquet_product2.price}
        response = self.client.get(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        qs = Product.objects.active().filter(
            price__gte=self.bouquet_product1.price,
            price__lte=self.bouquet_product2.price
        )
        self.assertEqual(
            response.data['results'],
            ProductSerializer(qs, many=True, context=self.get_context(url)).data
        )

    def test_create_present_not_superuser(self):
        url = reverse('api:product-create-present')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_bouquet_not_superuser(self):
        url = reverse('api:product-create-bouquet')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

