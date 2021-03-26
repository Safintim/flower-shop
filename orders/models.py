from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Sum

from cart.models import Cart, CartProduct
from core.models import CreationModificationModel
from main.models import Product, Bouquet


class OrderProduct(CreationModificationModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    bouquet = models.ForeignKey(Bouquet, on_delete=models.CASCADE, verbose_name='Букет', blank=True, null=True)
    price = models.DecimalField('Цена', max_digits=9, decimal_places=2, default=0, blank=True)
    qty = models.PositiveIntegerField('Количество', default=1, blank=True, validators=[MinValueValidator(1)])
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE, related_name='products', verbose_name='Заказ')

    class Meta:
        verbose_name = 'Продукт заказа'
        verbose_name_plural = 'Продукты заказов'

    def __str__(self):
        return f'{self.order.user.phone} - {self.product.title}'


class Order(CreationModificationModel):
    class Status(models.TextChoices):
        NEW = 'NEW', 'Новый'
        CANCEL = 'CANCEL', 'Отмена'
        END = 'END', 'Завершен'

    class DeliveryMethod(models.TextChoices):
        DELIVERY = 'DELIVERY', 'Доставка'
        PICKUP = 'PICKUP', 'Самовызов, скидка 10%'

    class Postcard(models.TextChoices):
        YES = 'YES_POSTCARD', 'Приложить'
        NO = 'NO_POSTCARD', 'Без открытки'

    class Callback(models.TextChoices):
        NO = 'NO_CALL_BACK', 'Везти без звонка в указанный промежуток времени'
        YES = 'YES_CALL_BACK', 'Позвонить получателю для уточнения адреса'

    class Recipient(models.TextChoices):
        IAM = 'RECIPIENT_IAM', 'Получаю я сам(-а)'
        OTHER = 'RECIPIENT_OTHER', 'Указать получателя'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders', verbose_name='Пользователь')
    recipient = models.CharField('Контакты получателя', choices=Recipient.choices, max_length=15, default=Recipient.IAM)
    recipient_name = models.CharField('Имя получателя', max_length=200, blank=True, null=True)
    recipient_phone = models.CharField('Номер телефона получателя', max_length=20, blank=True, null=True)
    recipient_address = models.CharField('Адрес', max_length=250, blank=True, null=True)
    recipient_call = models.CharField('Адрес получателя', choices=Callback.choices, max_length=23, default=Callback.NO)
    delivery_type = models.CharField('Способ доставки', choices=DeliveryMethod.choices, max_length=8, default=DeliveryMethod.PICKUP)
    delivery_date = models.DateField('Дата')
    delivery_time = models.TimeField('Время доставки', null=True, blank=True)
    postcard = models.CharField('Открытка', choices=Postcard.choices, max_length=12, default=Postcard.NO)
    postcard_text = models.TextField('Текст открытки', null=True, blank=True)
    comment = models.TextField('Комментарий', null=True, blank=True)
    status = models.CharField('Статус', choices=Status.choices, max_length=6, default=Status.NEW)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-created_at',)

    def __str__(self):
        return f'Заказ {self.id}'

    def create_order_products(self):
        cart_products = CartProduct.objects.filter(cart__user=self.user)
        order_products = [
            OrderProduct(
                product=cart_product.product,
                qty=cart_product.qty,
                bouquet=cart_product.bouquet,
                price=cart_product.price,
                order=self
            )
            for cart_product in cart_products]

        OrderProduct.objects.bulk_create(order_products)
        cart_products.delete()

    @property
    def price_total(self):
        return self.products.aggregate(total=Sum('price'))['total']
