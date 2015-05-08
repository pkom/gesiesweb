# -*- encoding: utf-8 -*-

from django.db import models
from django.utils.text import slugify

from model_utils.models import TimeStampedModel

from cursos.models import Curso
from profesores.models import CursoProfesor

class Departamento(TimeStampedModel):
    departamento = models.CharField(max_length=100, db_index=True, unique=True)
    descripcion = models.TextField(max_length=100, blank=True)
    slug = models.SlugField(unique=True, max_length=100)

    def __unicode__(self):
        return u"%s" % self.departamento

    def save(self, *args, **kwargs):
        self.slug = slugify(self.departamento)
        super(Departamento, self).save(*args, **kwargs)

    class Meta:
        ordering = [ 'departamento' ]


class CursoDepartamento(TimeStampedModel):
    curso = models.ForeignKey(Curso, related_name='cursodepartamentos')
    departamento = models.ForeignKey(Departamento, related_name='departamentos')
    jefe = models.ForeignKey(CursoProfesor, null=True, blank=True, related_name='jefes')

    def __unicode__(self):
        return u"%s - %s (%s)" % (self.curso, self.departamento, self.jefe if self.jefe else u'Sin jefe asignado')

    class Meta:
        unique_together = (("curso", "departamento"),)
        ordering = [ 'curso__curso', 'departamento__departamento' ]

class DepartamentoProfesor(TimeStampedModel):
    cursodepartamento = models.ForeignKey(CursoDepartamento, related_name='cursodepartamentos')
    cursoprofesor = models.ForeignKey(CursoProfesor, related_name='cursoprofesores')

    def __unicode__(self):
        return u"%s - %s" % (self.cursodepartamento, self.cursoprofesor)

    class Meta:
        unique_together = (("cursodepartamento", "cursoprofesor"),)
        ordering = [ 'cursodepartamento__curso__curso', 'cursodepartamento__departamento__departamento',
                     'cursoprofesor__profesor__user__last_name', 'cursoprofesor__profesor__user__first_name' ]