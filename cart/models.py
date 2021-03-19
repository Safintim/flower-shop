from django.conf import settings
from django.db import models

from main.models import Product


class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    qty = models.PositiveIntegerField('Количество', default=1, blank=True)
    cart = models.ForeignKey('cart.Cart', on_delete=models.CASCADE, verbose_name='Корзина')

    class Meta:
        verbose_name = 'Продукт корзины'
        verbose_name_plural = 'Продукты корзин'

    def __str__(self):
        return f'{self.cart.user.phone} - {self.product.title}'

    # def get


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'{self.id} - {self.user.phone}'
