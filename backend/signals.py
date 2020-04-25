from django.dispatch import receiver
from django.db.models.signals import post_save

from app import models


@receiver(post_save, sender=models.Product)
def calculate_price(sender, instance, *args, **kwargs):

    coefficient = (100 - instance.discount) / 100

