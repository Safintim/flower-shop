from django.conf import settings
from django.db import models

from core.models import ActiveQuerySet

from django_random_queryset.queryset import RandomQuerySet


class ReviewQuerySet(ActiveQuerySet, RandomQuerySet):
    pass


class Review(models.Model):
    phone = models.CharField('Номер телефона', max_length=200, blank=True, null=True)
    name = models.CharField('Имя', max_length=200)
    city = models.CharField('Город', max_length=200, blank=True, null=True)
    image = models.ImageField('Изображение', upload_to=settings.IMAGE_REVIEW_UPLOAD_PATH, blank=True, null=True)
    social_link = models.URLField('Ссылка на соц сеть', max_length=200, blank=True, null=True)
    text = models.TextField('Отзыв', blank=True, null=True)
    is_active = models.BooleanField('Активно', default=False)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    objects = ReviewQuerySet.as_manager()

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.name}'
