import random
from string import digits

from django.db import models
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField
from transliterate import translit


class ActiveQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)


class CreationModificationModel(models.Model):
    created_at = models.DateTimeField('Создан', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлен', auto_now=True)

    class Meta:
        abstract = True


class SlugifyMixin:
    slug_source_field = None
    slug_target_field = None

    def save(self, *args, **kwargs):
        slug = translit(slugify(getattr(self, self.slug_source_field), allow_unicode=True), reversed=True)

        model = self.__class__
        while model.objects.exclude(pk=self.pk).filter(slug=slug).exists():
            new_slug = translit(slugify(getattr(self, self.slug_source_field), allow_unicode=True), reversed=True)
            slug = '{}-{}'.format(new_slug, random.choice(digits))

        setattr(self, self.slug_target_field, slug)
        super().save(*args, **kwargs)


class Configuration(CreationModificationModel):
    singleton_instance_id = 1
    bouquet_price_coefficient = models.FloatField('Наценка на цветы', default=1)

    def save(self, *args, **kwargs):
        self.pk = self.singleton_instance_id
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()

    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки'

    def __str__(self):
        return 'Настройки'


class Callback(CreationModificationModel):
    phone = PhoneNumberField(verbose_name='Номер телефона')
    is_new = models.BooleanField('Новая заявка', default=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Перезвоните мне'
        ordering = ('-created_at', )

    def __str__(self):
        return self.phone.raw_input
