from django.db import models
from django.db.models import Sum, F


class Category(models.Model):
    title = models.CharField('Название', max_length=100)
    slug = models.SlugField('Слаг', unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Reason(models.Model):
    title = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Повод'
        verbose_name_plural = 'Поводы'

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.title


class Product(models.Model):
    TYPE_PRESENT = 'PRESENT'
    TYPE_BOUQUET = 'BOUQUET'
    TYPE_CHOICE = (
        (TYPE_PRESENT, 'Подарок'),
        (TYPE_BOUQUET, 'Букет'),
    )
    type = models.CharField('Тип', choices=TYPE_CHOICE, max_length=12)
    title = models.CharField('Название', max_length=200)
    slug = models.SlugField('Слаг', unique=True)
    price = models.DecimalField('Цена', max_digits=9, decimal_places=2, default=0, blank=True)
    image = models.ImageField('Изображение', blank=True)
    is_active = models.BooleanField('Активный', default=False)
    discount = models.FloatField('Скидка', default=0, blank=True)
    categories = models.ManyToManyField(Category, verbose_name='Категории')
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Цвет')
    reasons = models.ManyToManyField(Reason, blank=True, verbose_name='Поводы')
    bouquets = models.ManyToManyField('main.Bouquet', verbose_name='Букеты', blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title


class Flower(models.Model):
    title = models.CharField('Название', max_length=100)
    price = models.DecimalField('Цена', max_digits=9, decimal_places=2)
    is_add_filter = models.BooleanField('Добавить в фильтр', default=True)

    class Meta:
        verbose_name = 'Цветок'
        verbose_name_plural = 'Цветы'
        ordering = ('title',)

    def __str__(self):
        return self.title


class Bouquet(models.Model):
    SIZE_SM = 'SMALL'
    SIZE_MD = 'MIDDLE'
    SIZE_BG = 'BIG'
    SIZE_CHOICE = (
        (SIZE_SM, 'Маленький'),
        (SIZE_MD, 'Средний (как на фото)'),
        (SIZE_BG, 'Большой'),
    )
    size = models.CharField('Размер', choices=SIZE_CHOICE, max_length=7)
    title = models.CharField('Название', max_length=100)
    price = models.DecimalField('Цена', max_digits=9, decimal_places=2, default=0, blank=True)
    flowers = models.ManyToManyField(
        Flower,
        through='main.BouquetFlower',
        verbose_name='Цветы',
        blank=True
    )

    class Meta:
        verbose_name = 'Букет'
        verbose_name_plural = 'Букеты'
        ordering = ('title',)

    def __str__(self):
        return self.title

    @staticmethod
    def calculate_bouquet_price(bouquet):
        bouquet_price = BouquetFlower.objects.filter(
            bouquet=bouquet,
        ).aggregate(
            total=Sum(F('count') * F('flower__price'), output_field=models.DecimalField()))['total']
        return bouquet_price


class BouquetFlower(models.Model):
    count = models.PositiveIntegerField('Количество', default=0)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, verbose_name='Цветок')
    bouquet = models.ForeignKey(Bouquet, on_delete=models.CASCADE, verbose_name='Букет')

    class Meta:
        verbose_name = 'Цветок'
        verbose_name_plural = 'Цветы в средних букетах'

    def __str__(self):
        return f'{self.flower} - {self.bouquet}'
