# -*- encoding: utf-8 -*-

from django.db import models
from model_utils.models import TimeStampedModel

from sorl.thumbnail import ImageField

from cursos.models import Curso

class Alumno(TimeStampedModel):

    nie = models.CharField(unique=True, max_length=15, db_index=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    usuario_rayuela = models.CharField(max_length=20, blank=True)
    foto = ImageField(upload_to='alumnos', blank=True, default='')


    def __unicode__(self):
        return u"%s, %s" % (self.apellidos, self.nombre)

    class Meta:
        index_together = (("apellidos", "nombre"),)
        ordering = ['apellidos', 'nombre' ]

class CursoAlumno(TimeStampedModel):
    curso = models.ForeignKey(Curso)
    alumno = models.ForeignKey(Alumno)

    def __unicode__(self):
        return u"%s - %s" % (self.curso, self.alumno)

    class Meta:
        unique_together = (("curso", "alumno"),)
        ordering = ['alumno__apellidos', 'alumno__nombre' ]
