from django.db import models

from model_utils.models import TimeStampedModel

from cursos.models import Curso
from profesores.models import CursoProfesor

class Departamento(TimeStampedModel):
    departamento = models.CharField(max_length=50, db_index=True)
    descripcion = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return self.departamento

class CursoDepartamento(TimeStampedModel):
    curso = models.ForeignKey(Curso)
    departamento = models.ForeignKey(Departamento)
    jefe = models.ForeignKey(CursoProfesor, null=True, blank=True)

    def __unicode__(self):
        return "%s - %s (%s)" % (self.curso, self.departamento, self.jefe)

    class Meta:
        unique_together = (("curso", "departamento"),)

class DepartamentoProfesor(TimeStampedModel):
    departamento = models.ForeignKey(CursoDepartamento)
    profesor = models.ForeignKey(CursoProfesor)

    def __unicode__(self):
        return "%s - %s" % (self.departamento, self.profesor)

    class Meta:
        unique_together = (("departamento", "profesor"),)