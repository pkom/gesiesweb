from django.db import models
from django.utils import timezone

from model_utils.models import TimeStampedModel

from alumnos.models import CursoAlumno
from profesores.models import CursoProfesor

class Parte(TimeStampedModel):

    cursoalumno = models.ForeignKey(CursoAlumno)
    cursoprofesor = models.ForeignKey(CursoProfesor)
    fecha = models.DateField(null=False, default= timezone.now())
    parte = models.TextField(blank=False)
    con_parte = models.BooleanField(default=False)
    comunicado = models.BooleanField(default=False)
    cerrado = models.BooleanField(default=False)

    def __unicode__(self):
        return u"%s - %s" % (self.cursoalumno, self.cursoprofesor)

    class Meta:
        ordering = ['-created' ]


class ParteSeguimiento(TimeStampedModel):

    parte = models.ForeignKey(Parte)
    profesor = models.ForeignKey(CursoProfesor)
    seguimiento = models.TextField(blank=False)



