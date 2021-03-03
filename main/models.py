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
    price = models.DecimalField('Цена', max_digits=9, decimal_places=2, default=0, blank=True)
    image = models.ImageField('Изображение', blank=True)
    is_active = models.BooleanField('Активный', default=False)
    discount = models.FloatField('Скидка', default=0, blank=True)
    categories = models.ManyToManyField(Category, verbose_name='Категории')
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Цвет')
    reasons = models.ManyToManyField(Reason, blank=True, verbose_name='Поводы')

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


class Bouquet(Product):
    small_size = models.ManyToManyField(
        Flower,
        related_name='sm_size',
        through='main.BouquetFlowerSmall',
        verbose_name='Цветы',
        blank=False
    )
    middle_size = models.ManyToManyField(
        Flower,
        related_name='md_size',
        through='main.BouquetFlowerMiddle',
        verbose_name='Цветы',
        blank=False
    )
    big_size = models.ManyToManyField(
        Flower,
        related_name='bg_size',
        through='main.BouquetFlowerBig',
        verbose_name='Цветы',
        blank=True
    )

    class Meta:
        verbose_name = 'Букет'
        verbose_name_plural = 'Букеты'
        ordering = ('title',)

    def __str__(self):
        return self.title


class BouquetFlowerMiddle(models.Model):
    count = models.PositiveIntegerField('Количество', default=0)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, verbose_name='Цветок', )
    bouquet = models.ForeignKey(Bouquet, on_delete=models.CASCADE, verbose_name='Букет', )

    class Meta:
        verbose_name = 'Цветок'
        verbose_name_plural = 'Цветы в средних букетах'

    def __str__(self):
        return f'{self.flower} - {self.bouquet}'


class BouquetFlowerSmall(BouquetFlowerMiddle):
    class Meta:
        proxy = True
        verbose_name = 'Цветок'
        verbose_name_plural = 'Цветы в маленьких букетах'


class BouquetFlowerBig(BouquetFlowerMiddle):
    class Meta:
        proxy = True
        verbose_name = 'Цветок'
        verbose_name_plural = 'Цветы в больших букетах'
