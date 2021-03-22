from django.conf import settings
from django.db import models

from cart.models import Cart, CartProduct
from main.models import Product


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    price = models.DecimalField('Цена', max_digits=9, decimal_places=2, default=0, blank=True)
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE, related_name='products', verbose_name='Заказ')

    class Meta:
        verbose_name = 'Продукт заказа'
        verbose_name_plural = 'Продукты заказов'

    def __str__(self):
        return f'{self.order.user.phone} - {self.product.title}'


class Order(models.Model):
    STATUS_NEW = 'NEW'
    STATUS_CANCEL = 'CANCEL'
    STATUS_END = 'END'
    DELIVERY = 'DELIVERY'
    PICKUP = 'PICKUP'
    NO_POSTCARD = 'NO_POSTCARD'
    YES_POSTCARD = 'YES_POSTCARD'
    RECIPIENT_IAM = 'RECIPIENT_IAM'
    RECIPIENT_OTHER = 'RECIPIENT_OTHER'
    RECIPIENT_CALL_BACK = 'RECIPIENT_CALL_BACK'
    RECIPIENT_NOT_CALL_BACK = 'RECIPIENT_NOT_CALL_BACK'
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    RECIPIENT_CHOICE = (
        (RECIPIENT_IAM, 'Получаю я сам(-а)'),
        (RECIPIENT_OTHER, 'Указать получателя'),
    )
    recipient = models.CharField('Контакты получателя', choices=RECIPIENT_CHOICE, max_length=15, default=RECIPIENT_IAM)
    recipient_name = models.CharField('Имя получателя', max_length=200, blank=True, null=True)
    recipient_phone = models.CharField('Номер телефона получателя', max_length=20, blank=True, null=True)
    recipient_address = models.CharField('Адрес', max_length=250, blank=True, null=True)
    RECIPIENT_CALL_CHOICE = (
        (RECIPIENT_CALL_BACK, 'Везти без звонка в указанный промежуток времени'),
        (RECIPIENT_NOT_CALL_BACK, 'Позвонить получателю для уточнения адреса'),
    )
    recipient_call = models.CharField('Адрес получателя', choices=RECIPIENT_CALL_CHOICE, max_length=23, default=RECIPIENT_NOT_CALL_BACK)
    DELIVERY_CHOICE = (
        (DELIVERY, 'Доставка'),
        (PICKUP, 'Самовызов, скидка 10%'),
    )
    delivery_type = models.CharField('Способ доставки', choices=DELIVERY_CHOICE, max_length=8, default=PICKUP)
    delivery_date = models.DateField('Дата')
    delivery_time = models.TimeField('Время доставки', null=True, blank=True)
    POSTCARD_CHOICE = (
        (YES_POSTCARD, 'Приложить'),
        (NO_POSTCARD, 'Без открытки'),
    )
    postcard = models.CharField('Открытка', choices=POSTCARD_CHOICE, max_length=12, default=NO_POSTCARD)
    postcard_text = models.TextField('Текст открытки', null=True, blank=True)
    comment = models.TextField('Комментарий', null=True, blank=True)
    STATUS_CHOICE = (
        (STATUS_NEW, 'Новый'),
        (STATUS_CANCEL, 'Отмена'),
        (STATUS_END, 'Завершен'),
    )
    status = models.CharField('Статус', choices=STATUS_CHOICE, max_length=6, default=STATUS_NEW)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-created_at',)

    def __str__(self):
        return f'Заказ {self.id}'

    def create_order_products(self):
        cart_products = CartProduct.objects.filter(user=self.user)
        order_products = [
            OrderProduct.objects.create(
                product=cart_product.product,
                qty=cart_product.qty,
                price=cart_product.price,
                order=self
            )
            for cart_product in cart_products]

        OrderProduct.objects.bulk_create(*order_products)
        cart_products.delete()
