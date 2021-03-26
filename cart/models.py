from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import F, Sum

from core.models import CreationModificationModel
from main.models import Product, Bouquet


class CartProduct(CreationModificationModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    bouquet = models.ForeignKey(Bouquet, on_delete=models.CASCADE, verbose_name='Букет', blank=True, null=True)
    qty = models.PositiveIntegerField('Количество', default=1, blank=True, validators=[MinValueValidator(1)])
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

    def add_product(self, product, bouquet_size=None):

        if product.is_bouquet:
            cart_product = self.products.filter(product=product, bouquet__size=bouquet_size).first()
        else:
            cart_product = self.products.filter(product=product).first()

        if cart_product:
            cart_product.qty += 1
            cart_product.save()
        else:
            bouquet = product.get_bouquet_by_size(bouquet_size)
            cart_product = CartProduct.objects.create(cart=self, product=product, bouquet=bouquet)

        return cart_product
