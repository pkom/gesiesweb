from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel

from cursos.models import Curso

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, **kwargs):
    if kwargs.get('created', False):
        Profesor.objects.get_or_create(user=kwargs.get('instance'))

def upload_to(instance, filename):
    return '/'.join(['profesores', instance.user.username, filename])


class Profesor(TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, db_index=True)
    dni = models.CharField(blank=True, max_length=20, default='', db_index=True)
    usuario_rayuela = models.CharField(blank=True, max_length=20, default='')
    foto = models.ImageField(upload_to=upload_to, blank=True, default='')
    es_usuario = models.BooleanField(default=False)
    id_usuario = models.CharField(blank=True, max_length=20, default='')

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "profesores"

class CursoProfesor(TimeStampedModel):
    curso = models.ForeignKey(Curso)
    profesor = models.ForeignKey(Profesor)

    def __unicode__(self):
        return "%s - %s" % (self.curso, self.profesor)

    class Meta:
        unique_together = (("curso", "profesor"),)