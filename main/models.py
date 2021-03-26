from django.conf import settings
from django.db import models
from django.db.models import Sum, F

from django_random_queryset.queryset import RandomQuerySet

from core.models import ActiveQuerySet, CreationModificationModel, Configuration, SlugifyMixin


class CategoryQuerySet(ActiveQuerySet):
    def parent_null(self):
        return self.filter(parent__isnull=True)


class CommonFields(models.Model):
    title = models.CharField('Название', max_length=200)

    class Meta:
        abstract = True


class Category(SlugifyMixin, CommonFields):
    slug = models.SlugField('Слаг', unique=True, blank=True)
    parent = models.ForeignKey(
        'main.Category',
        on_delete=models.SET_NULL,
        related_name='children',
        null=True,
        blank=True,
        verbose_name='Родительская'
    )
    is_active = models.BooleanField('Активна', default=True)
    objects = CategoryQuerySet.as_manager()

    slug_source_field = 'title'
    slug_target_field = 'slug'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Reason(CommonFields):

    class Meta:
        verbose_name = 'Повод'
        verbose_name_plural = 'Поводы'

    def __str__(self):
        return self.title


class Color(CommonFields):

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.title


class ProductQuerySet(ActiveQuerySet, RandomQuerySet):
    def presents(self):
        return self.filter(type=Product.Type.PRESENT)

    def bouquets(self):
        return self.filter(type=Product.Type.BOUQUET)

    def hits(self):
        return self.filter(is_hit=True)

    def new(self):
        return self.filter(is_new=True)


class Product(SlugifyMixin, CreationModificationModel, CommonFields):
    class Type(models.TextChoices):
        PRESENT = 'PRESENT', 'Подарок'
        BOUQUET = 'BOUQUET', 'Букет'

    type = models.CharField('Тип', choices=Type.choices, max_length=12)
    slug = models.SlugField('Слаг', unique=True, blank=True)
    price = models.DecimalField('Цена', max_digits=9, decimal_places=2, default=0, blank=True)
    small_image = models.ImageField('Изображение(маленькое)', upload_to=settings.IMAGE_UPLOAD_PATH, help_text='Размер 372х372')
    big_image = models.ImageField('Изображение(большое)', upload_to=settings.IMAGE_UPLOAD_PATH, help_text='Размер 640x640')
    is_active = models.BooleanField('Активный', default=False, db_index=True)
    is_hit = models.BooleanField('Хит', default=False, db_index=True)
    is_new = models.BooleanField('Новинка', default=False, db_index=True)
    discount = models.PositiveIntegerField('Скидка', default=0, blank=True)
    categories = models.ManyToManyField(Category, verbose_name='Категории', db_index=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Цвет', db_index=True)
    reasons = models.ManyToManyField(Reason, blank=True, verbose_name='Поводы', db_index=True)
    bouquets = models.ManyToManyField('main.Bouquet', verbose_name='Букеты', blank=True, db_index=True)
    objects = ProductQuerySet.as_manager()

    slug_source_field = 'title'
    slug_target_field = 'slug'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title

    @property
    def is_bouquet(self):
        return self.type == self.Type.BOUQUET

    @property
    def is_present(self):
        return self.type == self.Type.PRESENT

    @property
    def cheap_bouquet(self):
        return self.bouquets.order_by('price').first()

    def get_small_bouquet(self):
        return self.bouquets.filter(size=Bouquet.Size.SM).first()

    def get_middle_bouquet(self):
        return self.bouquets.filter(size=Bouquet.Size.MD).first()

    def get_big_bouquet(self):
        return self.bouquets.filter(size=Bouquet.Size.BG).first()

    def get_bouquet_by_size(self, size):
        return self.bouquets.filter(size=size).first()

    def get_small_bouquet_price(self):
        bouquet = self.get_small_bouquet()
        return bouquet.price if bouquet else '-'
    get_small_bouquet_price.short_description = 'Цена маленького букета'

    def get_middle_bouquet_price(self):
        bouquet = self.get_middle_bouquet()
        return bouquet.price if bouquet else '-'
    get_middle_bouquet_price.short_description = 'Цена среднего букета'

    def get_big_bouquet_price(self):
        bouquet = self.get_big_bouquet()
        return bouquet.price if bouquet else '-'
    get_big_bouquet_price.short_description = 'Цена большого букета'


class Flower(CreationModificationModel, CommonFields):
    price = models.DecimalField('Цена', max_digits=9, decimal_places=2)
    is_add_filter = models.BooleanField('Добавить в фильтр', default=True)

    class Meta:
        verbose_name = 'Цветок'
        verbose_name_plural = 'Цветы'
        ordering = ('title',)

    def __str__(self):
        return self.title


class Bouquet(CreationModificationModel):
    class Size(models.TextChoices):
        SM = 'SMALL', 'Маленький'
        MD = 'MIDDLE', 'Средний (как на фото)'
        BG = 'BIG', 'Большой'

    size = models.CharField('Размер', choices=Size.choices, max_length=7, db_index=True)
    title = models.CharField('Название', max_length=100, db_index=True)
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
        coefficient = Configuration.load().bouquet_price_coefficient
        bouquet_price = BouquetFlower.objects.filter(
            bouquet=bouquet,
        ).aggregate(total=Sum(
            F('count') * F('flower__price') * coefficient,
            output_field=models.DecimalField())
        )['total']
        return bouquet_price


class BouquetFlower(CreationModificationModel):
    count = models.PositiveIntegerField('Количество', default=0)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, verbose_name='Цветок')
    bouquet = models.ForeignKey(Bouquet, on_delete=models.CASCADE, verbose_name='Букет')

    class Meta:
        verbose_name = 'Цветок'
        verbose_name_plural = 'Цветы в средних букетах'

    def __str__(self):
        return f'{self.flower} - {self.bouquet}'
