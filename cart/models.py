from django.conf import settings
from django.db import models
from django.db.models import F, Sum

from main.models import Product, Bouquet


class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    bouquet = models.ForeignKey(Bouquet, on_delete=models.CASCADE, verbose_name='Букет', blank=True, null=True)
    qty = models.PositiveIntegerField('Количество', default=1, blank=True)
    cart = models.ForeignKey('cart.Cart', on_delete=models.CASCADE, verbose_name='Корзина', related_name='products')

    class Meta:
        verbose_name = 'Продукт корзины'
        verbose_name_plural = 'Продукты корзин'

    def __str__(self):
        return f'{self.cart.user.phone} - {self.product.title}'

    @property
    def price(self):
        if self.product.is_bouquet:
            price = self.bouquet.price
        else:
            price = self.product.price
        return price * self.qty


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'{self.id} - {self.user.phone}'

    @property
    def product_total(self):
        return self.products.count()

    @property
    def price_total(self):
        bouquets_price = self.products.filter(bouquet__isnull=False).aggregate(
            total=Sum(F('bouquet__price') * F('qty'), output_field=models.DecimalField())
        )['total'] or 0
        presents_price = self.products.filter(bouquet__isnull=True).aggregate(
            total=Sum(F('product__price') * F('qty'), output_field=models.DecimalField())
        )['total'] or 0
        return bouquets_price + presents_price
