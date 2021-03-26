from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class ActiveQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)


class CreationModificationModel(models.Model):
    created_at = models.DateTimeField('Создан', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлен', auto_now=True)

    class Meta:
        abstract = True


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
