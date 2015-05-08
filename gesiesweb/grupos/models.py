# -*- encoding: utf-8 -*-

from django.db import models
from django.utils.text import slugify

from model_utils.models import TimeStampedModel

from sorl.thumbnail import get_thumbnail

from cursos.models import Curso
from profesores.models import CursoProfesor
from alumnos.models import CursoAlumno

class Grupo(TimeStampedModel):

    grupo = models.CharField(max_length=10, db_index=True, unique=True)
    descripcion = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(unique=True, max_length=10)

    def __unicode__(self):
        return u"%s" % self.grupo

    def save(self, *args, **kwargs):
        self.slug = slugify(self.grupo)
        super(Grupo, self).save(*args, **kwargs)

    class Meta:
        ordering = [ 'grupo' ]


class CursoGrupo(TimeStampedModel):

    curso = models.ForeignKey(Curso, related_name='cursogrupos')
    grupo = models.ForeignKey(Grupo, related_name='grupos')
    tutor = models.ForeignKey(CursoProfesor, null=True, blank=True, related_name='tutores')

    def __unicode__(self):
        return u"%s - %s (%s)" % (self.curso, self.grupo, self.tutor if self.tutor else u'Sin tutoría asignada')

    def get_nombre_completo(self):
        return self.tutor.get_nombre_completo()

    class Meta:
        unique_together = (("curso", "grupo"),)
        ordering = [ 'curso__curso', 'grupo__grupo' ]


class GrupoAlumno(TimeStampedModel):

    cursogrupo = models.ForeignKey(CursoGrupo, related_name='grupoalumnos')
    cursoalumno = models.ForeignKey(CursoAlumno, related_name='alumnos')

    def __unicode__(self):
        return u"%s - %s" % (self.cursogrupo, self.cursoalumno)

    def get_nombre_completo(self):

        return self.cursoalumno.alumno.get_nombre_completo()

    def get_nombre_grupo(self):

        return u"%s" % (self.cursogrupo.grupo.grupo)

    def get_foto(self):

        if self.cursoalumno.alumno.foto:
            return u"%s" % (get_thumbnail(self.cursoalumno.alumno.foto, '50x40').url)
        else:
            return u""


    class Meta:
        unique_together = (("cursogrupo", "cursoalumno"),)
        ordering = [ 'cursogrupo__curso__curso', 'cursogrupo__grupo__grupo',
                     'cursoalumno__alumno__apellidos', 'cursoalumno__alumno__nombre']


class GrupoProfesor(TimeStampedModel):

    cursogrupo = models.ForeignKey(CursoGrupo, related_name='grupoprofesores')
    cursoprofesor = models.ForeignKey(CursoProfesor, related_name='profesores')

    def __unicode__(self):
        return u"%s - %s" % (self.cursogrupo, self.cursoprofesor)

    class Meta:
        unique_together = (("cursogrupo", "cursoprofesor"),)
        ordering = [ 'cursogrupo__curso__curso', 'cursogrupo__grupo__grupo',
                     'cursoprofesor__profesor__user__last_name', 'cursoprofesor__profesor__user__first_name' ]
