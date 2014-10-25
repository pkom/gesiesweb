from django.dispatch import receiver
from django.db.models.signals import post_save

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, **kwargs):
    if kwargs.get('created', False):
        Usuario.objects.get_or_create(user=kwargs.get('instance'))

def upload_to(instance, filename):
    return '/'.join(['usuarios', instance.user.username, filename])


class Usuario(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, db_index=True)
    dni = models.CharField(blank=True, max_length=20)
    usuario_rayuela = models.CharField(blank=True, max_length=20)
    foto = models.ImageField(upload_to=upload_to, blank=True)
