# -*- encoding: utf-8 -*-

from django.db import models
from model_utils.models import TimeStampedModel

from sorl.thumbnail import ImageField, get_thumbnail

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

    def get_nombre_completo(self):

        return u"%s, %s" % (self.apellidos, self.nombre)

    class Meta:

        index_together = (("apellidos", "nombre"),)
        ordering = ['apellidos', 'nombre' ]

class CursoAlumno(TimeStampedModel):

    curso = models.ForeignKey(Curso, related_name='cursoalumnos')
    alumno = models.ForeignKey(Alumno, related_name='alumnos')

    def __unicode__(self):

        return u"%s - %s" % (self.curso, self.alumno)

    def get_nombre_completo(self):

        return self.alumno.get_nombre_completo()

    def get_foto(self):

        if self.alumno.foto:
            return u"%s" % (get_thumbnail(self.alumno.foto, '50x40').url)
        else:
            return u""

    class Meta:
        unique_together = (("curso", "alumno"),)
        ordering = ['alumno__apellidos', 'alumno__nombre' ]
