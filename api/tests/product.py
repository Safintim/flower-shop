import tempfile
from PIL import Image
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from api.serializers import ProductSerializer
from main.models import Product, Flower, BouquetFlower, Bouquet, Category, Color, Reason

User = get_user_model()


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

        self.user = User.objects.create_superuser(phone='897657653412', password='1234567')

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

    def get_image(self, sizes):
        image = Image.new('RGB', sizes)
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        tmp_file.seek(0)
        return tmp_file

    def get_small_image(self):
        return self.get_image((372, 372))

    def get_big_image(self):
        return self.get_image((640, 640))

    def test_create_present_valid(self):
        self.client.force_login(user=self.user)
        data = {
            'title': 'Конфеты Rafaello',
            'price': 600,
            'discount': 5,
            'small_image': self.get_small_image(),
            'big_image': self.get_big_image(),
            'is_active': True,
            'is_new': True,
            'is_hit': True,
            'categories': [self.category2.pk],
            'reasons': [self.reason1.pk],
        }
        url = reverse('api:product-create-present')
        response = self.client.post(url, data=data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        product = Product.objects.filter(title=data['title']).first()
        self.assertTrue(product.small_image is not None)
        self.assertTrue(product.is_active)
        self.assertTrue(product.is_hit)
        self.assertEqual(product.type, Product.Type.PRESENT)

    def test_create_present_not_valid(self):
        self.client.force_login(user=self.user)
        data = {
            'title': 'Конфеты Rafaello',
            'price': 600,
            'small_image': self.get_image((100, 100)),
            'reasons': [self.reason1.pk],
        }
        url = reverse('api:product-create-present')
        response = self.client.post(url, data=data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('small_image' in response.data)
        self.assertTrue('big_image' in response.data)
        self.assertTrue('categories' in response.data)

    def test_create_bouquet_valid(self):
        self.client.force_login(user=self.user)
        data = {
            'title': 'Лучший Букет из пион',
            'discount': 5,
            'small_image': self.get_small_image(),
            'big_image': self.get_big_image(),
            'is_active': True,
            'is_new': True,
            'is_hit': True,
            'categories': [self.category2.pk],
            'reasons': [self.reason1.pk],
            'color': self.reason1.pk,
        }
        url = reverse('api:product-create-bouquet')
        response = self.client.post(url, data=data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        product = Product.objects.filter(title=data['title']).first()
        self.assertFalse(product.is_active)
        self.assertEqual(product.type, Product.Type.BOUQUET)

    def test_add_bouquets_valid(self):
        self.client.force_login(user=self.user)
        product = Product.objects.create(
            type=Product.Type.BOUQUET,
            title='Лучший Букет из пион',
        )

        data = {
            'SMALL': {
                'flowers': [
                    {
                        'count': 5,
                        'flower': self.flower1.pk
                    }
                ]
            },
            'MIDDLE': {
                'flowers': [
                    {
                        'count': 10,
                        'flower': self.flower2.pk
                    }
                ]
            },
        }

        url = reverse('api:product-add-bouquets', args=[product.pk])
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, ProductSerializer(product, context=self.get_context(url)).data)
        self.assertEqual(product.bouquets.count(), 2)
        self.assertEqual(product.get_small_bouquet().flowers.first(), self.flower1)
        self.assertEqual(product.get_middle_bouquet().flowers.first(), self.flower2)

    def test_add_bouquets_not_valid(self):
        self.client.force_login(user=self.user)
        product = Product.objects.create(
            type=Product.Type.BOUQUET,
            title='Лучший Букет из пион',
        )

        data = {
            'SMALL': {
                'flowers': [
                    {
                        'count': 5,
                        'flower': self.flower1.pk
                    }
                ]
            },
        }

        url = reverse('api:product-add-bouquets', args=[product.pk])
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('MIDDLE' in response.data)

    def test_add_bouquets_with_empty_flowers_not_valid(self):
        self.client.force_login(user=self.user)
        product = Product.objects.create(
            type=Product.Type.BOUQUET,
            title='Лучший Букет из пион',
        )

        data = {
            'MIDDLE': {
                'flowers': []
            },
        }

        url = reverse('api:product-add-bouquets', args=[product.pk])
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('MIDDLE' in response.data)
