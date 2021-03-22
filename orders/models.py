from django.conf import settings
from django.db import models

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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    recipient_name = models.CharField('Имя получателя', max_length=200, blank=True, null=True)
    recipient_phone = models.CharField('Номер телефона получателя', max_length=20, blank=True, null=True)
    recipient_address = models.CharField('Адрес получателя', max_length=250)
    STATUS_CHOICE = (
        (STATUS_NEW, 'Новый'),
        (STATUS_CANCEL, 'Отмена'),
        (STATUS_END, 'Завершен'),
    )
    status = models.CharField('Статус', choices=STATUS_CHOICE, max_length=200, default='NEW')
    comment = models.TextField('Комментарий к заказу', null=True, blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-created_at', )

    def __str__(self):
        return f'Заказ {self.id}'
