# -*- encoding: utf-8 -*-

from django.db import models
from model_utils.models import TimeStampedModel

from cursos.models import Curso
from profesores.models import CursoProfesor
from alumnos.models import CursoAlumno

class Grupo(TimeStampedModel):
    grupo = models.CharField(max_length=10, db_index=True, unique=True)
    descripcion = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return u"%s" % self.grupo

    class Meta:
        ordering = [ 'grupo' ]


class CursoGrupo(TimeStampedModel):
    curso = models.ForeignKey(Curso)
    grupo = models.ForeignKey(Grupo)
    tutor = models.ForeignKey(CursoProfesor, null=True, blank=True)

    def __unicode__(self):
        return u"%s - %s (%s)" % (self.curso, self.grupo, self.tutor if self.tutor else u'Sin tutoría asignada')

    class Meta:
        unique_together = (("curso", "grupo"),)
        ordering = [ 'curso__curso', 'grupo__grupo' ]


class GrupoAlumno(TimeStampedModel):
    cursogrupo = models.ForeignKey(CursoGrupo)
    cursoalumno = models.ForeignKey(CursoAlumno)

    def __unicode__(self):
        return u"%s - %s" % (self.cursogrupo, self.cursoalumno)

    class Meta:
        unique_together = (("cursogrupo", "cursoalumno"),)
        ordering = [ 'cursogrupo__curso__curso', 'cursogrupo__grupo__grupo',
                     'cursoalumno__alumno__apellidos', 'cursoalumno__alumno__nombre']


class GrupoProfesor(TimeStampedModel):
    cursogrupo = models.ForeignKey(CursoGrupo)
    cursoprofesor = models.ForeignKey(CursoProfesor)

    def __unicode__(self):
        return u"%s - %s" % (self.cursogrupo, self.cursoprofesor)

    class Meta:
        unique_together = (("cursogrupo", "cursoprofesor"),)
        ordering = [ 'cursogrupo__curso__curso', 'cursogrupo__grupo__grupo',
                     'cursoprofesor__profesor__user__last_name', 'cursoprofesor__profesor__user__first_name' ]
