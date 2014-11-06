# -*- encoding: utf-8 -*-

from django.db import models
from model_utils.models import TimeStampedModel

from cursos.models import Curso

class Alumno(TimeStampedModel):
    nie = models.CharField(unique=True, max_length=15, db_index=True)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    usuario_rayuela = models.CharField(max_length=20, blank=True)
    foto = models.ImageField(upload_to='alumnos', blank=True)

    def __unicode__(self):
        return u"%s, %s" % (self.apellidos, self.nombre)

    def foto_alumno(self):
        return """
        <img src ="%s"/>
        """ % self.foto.url

    foto_alumno.allow_tags = True

    class Meta:
        index_together = (("apellidos", "nombre"),)

class CursoAlumno(TimeStampedModel):
    curso = models.ForeignKey(Curso)
    alumno = models.ForeignKey(Alumno)

    def __unicode__(self):
        return u"%s" % self.alumno

    class Meta:
        unique_together = (("curso", "alumno"),)