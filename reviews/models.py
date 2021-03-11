from django.db import models

from core.models import ActiveQuerySet


class ReviewManager(models.Manager):
    def get_queryset(self):
        return ActiveQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()


class Review(models.Model):
    phone = models.CharField('Номер телефона', max_length=200, blank=True, null=True)
    name = models.CharField('Имя', max_length=200, blank=True, null=True)
    city = models.CharField('Город', max_length=200, blank=True, null=True)
    social_link = models.URLField('Ссылка на соц сеть', max_length=200, blank=True, null=True)
    text = models.TextField('Отзыв', blank=True, null=True)
    is_active = models.BooleanField('Активно', default=False)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    objects = ReviewManager()

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.name}'
