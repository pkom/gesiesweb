# -*- encoding: utf-8 -*-

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel

from sorl.thumbnail import ImageField, get_thumbnail

import django_auth_ldap.backend

from cursos.models import Curso

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, **kwargs):
    if kwargs.get('created', False):
        Profesor.objects.get_or_create(user=kwargs.get('instance'))

#en django 1.7 no funciona AUTH_PROFILE_MODULE actualizamos datos mediante este signal
def update_profesor(sender, user=None, ldap_user=None, **kwargs):

    # Remember that every attribute maps to a list of values
    dni = ldap_user.attrs.get("employeeNumber", [])
    uid = ldap_user.attrs.get("uid", [])
    profe = user.profesor
    if dni:
        profe.dni = dni[0]
    if uid:
        profe.usuario_rayuela = uid[0]
    profe.save()

django_auth_ldap.backend.populate_user.connect(update_profesor)


def upload_to(instance, filename):
    return '/'.join(['profesores', instance.user.username, filename])


class Profesor(TimeStampedModel):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, db_index=True, related_name='profesor')
    dni = models.CharField(blank=True, max_length=20, default='', db_index=True, unique=True)
    usuario_rayuela = models.CharField(blank=True, max_length=50, default='')
    foto = ImageField(upload_to=upload_to, blank=True, default='')
    es_usuario = models.BooleanField(default=False)
    id_usuario = models.CharField(blank=True, max_length=20, default='')

    def __unicode__(self):

        return u"%s, %s (%s)" % (self.user.last_name, self.user.first_name, self.user.username)

    def get_nombre_completo(self):

        return u"%s, %s" % (self.user.last_name, self.user.first_name)

    class Meta:

        ordering = [ 'user__last_name', 'user__first_name' ]


class CursoProfesor(TimeStampedModel):

    curso = models.ForeignKey(Curso, related_name='cursos')
    profesor = models.ForeignKey(Profesor, related_name='profesores')
    es_responsable = models.BooleanField(default=False)

    def __unicode__(self):

        return u"%s - %s" % (self.curso, self.profesor)

    def get_nombre_completo(self):

        return self.profesor.get_nombre_completo()

    def get_foto(self):

        if self.profesor.foto:
            return u"%s" % (get_thumbnail(self.profesor.foto, '50x40').url)
        else:
            return u""


    class Meta:
        unique_together = (("curso", "profesor"),)
        ordering = [ 'curso__curso', 'profesor__user__last_name', 'profesor__user__first_name' ]