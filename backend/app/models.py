from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField('Email', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id', )

    def __str__(self):
        return self.email


class City(models.Model):
    title = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ('title', )

    def __str__(self):
        return self.title


class Category(MPTTModel):
    title = models.CharField('Название', max_length=100, db_index=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Родительская категория',
        db_index=True,
    )

    class MPTTMeta:
        order_insertion_by = ('title', )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Flower(models.Model):
    title = models.CharField('Название', max_length=200)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    is_add_filter = models.BooleanField('Добавить в фильтр', default=True)

    class Meta:
        verbose_name = 'Цветок'
        verbose_name_plural = 'Цветы'
        ordering = ('title', )

    def __str__(self):
        return self.title


class BaseBouquet(models.Model):
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', blank=True, null=True)
    is_active = models.BooleanField('Активный', default=False)
    is_new = models.BooleanField('Новика', default=False)
    is_hit = models.BooleanField('Хит', default=False)
    discount = models.FloatField('Скидка', default=0)
    COLOR_CHOICE = (
        ('SOFT', 'Нежный'),
        ('BRIGHT', 'Яркий'),
    )
    color = models.CharField(
        'Цвет',
        max_length=6,
        blank=True,
        null=True,
        default=None,
    )
    height = models.PositiveIntegerField('Высота', default=0)
    width = models.PositiveIntegerField('Ширина', default=0)

    category = TreeManyToManyField(
        'app.Category',
        blank=True,
        verbose_name='Категории',
        db_index=True,
    )
    reason = models.ManyToManyField(
        'app.Reason',
        verbose_name='Поводы',
    )

    class Meta:
        verbose_name = 'Базовый Букет'
        verbose_name_plural = 'Букеты'
        ordering = ('title', )

    def __str__(self):
        return self.title


class Bouquet(models.Model):
    title = models.CharField('Название', max_length=200)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    SIZE_CHOICE = (
        ('SMALL', 'Маленький'),
        ('MEDIUM', 'Средний'),
        ('BIG', 'Большой'),
    )
    size = models.CharField(
        'Размер',
        choices=SIZE_CHOICE,
        max_length=200,
        default='MEDIUM',
    )

    base = models.ForeignKey(
        'app.BaseBouquet',
        on_delete=models.CASCADE,
        verbose_name='Базовый букет',
    )
    flowers = models.ManyToManyField(
        'app.Flower',
        through='app.BouquetFlower',
        verbose_name='Цветы',
    )

    class Meta:
        verbose_name = 'Букет'
        verbose_name_plural = 'Букеты'
        ordering = ('title', )

    def __str__(self):
        return self.title


class BouquetFlower(models.Model):
    count = models.PositiveIntegerField('Количество', default=0)
    flower = models.ForeignKey(
        'app.Flower',
        on_delete=models.CASCADE,
        verbose_name='Цветок',
    )
    bouquet = models.ForeignKey(
        'app.Bouquet',
        on_delete=models.CASCADE,
        verbose_name='Букет',
    )

    class Meta:
        verbose_name = 'Цветок'
        verbose_name_plural = 'Цветы'

    def __str__(self):
        return f'{self.flower} - {self.bouquet}'


class Reason(models.Model):
    title = models.CharField('Название', max_length=200)

    class Meta:
        verbose_name = 'Повод'
        verbose_name_plural = 'Поводы'

    def __str__(self):
        return f'{self.title}'


class Review(models.Model):
    phone = models.CharField(
        'Номер телефона',
        max_length=200,
        blank=True,
        null=True,
    )
    name = models.CharField(
        'Имя',
        max_length=200,
        blank=True,
        null=True,
    )
    city = models.CharField(
        'Город',
        max_length=200,
        blank=True,
        null=True,
    )
    social_link = models.CharField(
        'Ссылка на соц сеть',
        max_length=200,
        blank=True,
        null=True,
    )
    text = models.TextField(
        'Отзыв',
        blank=True,
        null=True,
    )
    rating = models.PositiveSmallIntegerField('Оценка', default=1)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    customer_name = models.CharField('Имя заказчика', max_length=200)
    customer_phone = models.CharField('Номер телефона заказчика', max_length=20)
    recipient_name = models.CharField(
        'Имя получателя',
        max_length=200,
        blank=True,
        null=True,
    )
    recipient_phone = models.CharField(
        'Номер телефона получателя',
        max_length=20,
        blank=True,
        null=True,
    )
    recipient_address = models.CharField(
        'Адрес получателя',
        max_length=250,
    )
    city = models.CharField('Город', max_length=100)
    is_paid = models.BooleanField('Оплачено', default=False)
    STATUS_CHOICE = (
        ('NEW', 'Новый'),
        ('CANCEL', 'Отмена'),
        ('END', 'Завершен'),
    )
    status = models.CharField(
        'Статус',
        choices=STATUS_CHOICE,
        max_length=200,
        default='NEW',
    )
    comment = models.TextField('Комментарий к заказу', null=True, blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-created_at', )

    def __str__(self):
        return f'Заказ {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(
        'app.Order',
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Заказ',
    )
    product = models.ForeignKey(
        'app.Bouquet',
        on_delete=models.CASCADE,
        verbose_name='Товар',
    )
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField('Количество', default=1)

    def get_cost(self):
        return self.price * self.quantity

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.order.id}'
