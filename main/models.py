from django.db import models


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
    title = models.CharField('Название', max_length=200)
    slug = models.SlugField('Слаг', unique=True)
    price = models.DecimalField('Цена', max_digits=9, decimal_places=2)
    image = models.ImageField('Изображение')
    is_active = models.BooleanField('Активный', default=False)
    discount = models.FloatField('Скидка', default=0)
    categories = models.ManyToManyField(Category, verbose_name='Категории')
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='Цвет')
    reasons = models.ManyToManyField(Reason, blank=False, verbose_name='Поводы')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title

