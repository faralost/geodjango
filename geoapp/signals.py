
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from geoapp.models import User, Farmer


@receiver(post_save, sender=User)
def update_farmer_signal(sender, instance, created, **kwargs):
    if kwargs['raw']:
        return
    if created:
        Farmer.objects.create(user=instance)
    instance.farmer.save()

