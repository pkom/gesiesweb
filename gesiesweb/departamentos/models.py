from django.db import models

from model_utils.models import TimeStampedModel

from cursos.models import Curso
from profesores.models import CursoProfesor

class Departamento(TimeStampedModel):
    departamento = models.CharField(max_length=100, db_index=True)
    descripcion = models.TextField(max_length=100, blank=True)

    def __unicode__(self):
        return u"%s" % self.departamento

class CursoDepartamento(TimeStampedModel):
    curso = models.ForeignKey(Curso)
    departamento = models.ForeignKey(Departamento)
    jefe = models.ForeignKey(CursoProfesor, null=True, blank=True)

    def __unicode__(self):
        return u"%s - %s (%s)" % (self.curso, self.departamento, self.jefe if self.jefe else 'Sin jefe asignado')

    class Meta:
        unique_together = (("curso", "departamento"),)

class DepartamentoProfesor(TimeStampedModel):
    cursodepartamento = models.ForeignKey(CursoDepartamento)
    cursoprofesor = models.ForeignKey(CursoProfesor)

    def __unicode__(self):
        return u"%s - %s" % (self.cursodepartamento, self.cursoprofesor)

    class Meta:
        unique_together = (("cursodepartamento", "cursoprofesor"),)