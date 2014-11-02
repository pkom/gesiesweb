from django.db import models
from model_utils.models import TimeStampedModel

from cursos.models import Curso
from profesores.models import CursoProfesor
from alumnos.models import CursoAlumno

class Grupo(TimeStampedModel):
    grupo = models.CharField(max_length=10, db_index=True)
    descripcion = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return self.grupo

class CursoGrupo(TimeStampedModel):
    curso = models.ForeignKey(Curso)
    grupo = models.ForeignKey(Grupo)
    tutor = models.ForeignKey(CursoProfesor, null=True, blank=True)

    def __unicode__(self):
        return "%s - %s (%s)" % (self.curso, self.grupo, self.tutor)

    class Meta:
        unique_together = (("curso", "grupo"),)

class GrupoAlumno(TimeStampedModel):
    grupo = models.ForeignKey(CursoGrupo)
    alumno = models.ForeignKey(CursoAlumno)

    def __unicode__(self):
        return "%s - %s" % (self.grupo, self.alumno)

    class Meta:
        unique_together = (("grupo", "alumno"),)

class GrupoProfesor(TimeStampedModel):
    grupo = models.ForeignKey(CursoGrupo)
    profesor = models.ForeignKey(CursoProfesor)

    def __unicode__(self):
        return "%s - %s" % (self.grupo, self.profesor)

    class Meta:
        unique_together = (("grupo", "profesor"),)