from django.db.models.signals import post_save
from django.dispatch import receiver

from main import models


@receiver(post_save, sender=models.Configuration)
@receiver(post_save, sender=models.Flower)
def update_bouquets_price(sender, instance, **kwargs):
    if sender.__name__ == 'Configuration':
        bouquets = models.Bouquet.objects.all()
    else:
        bouquets = models.Bouquet.objects.filter(flowers=instance)
    for b in bouquets:
        b.price = models.Bouquet.calculate_bouquet_price(b)
        b.save()
