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


    def parte_seguimientos(self):

        return self.parteseguimiento_set.all()

    def get_nombre_completo_profesor(self):

        return self.cursoprofesor.get_nombre_completo()

    def get_nombre_completo_alumno(self):

        return self.cursoalumno.get_nombre_completo()

    class Meta:

        ordering = ['-created' ]


class ParteSeguimiento(TimeStampedModel):

    parte = models.ForeignKey(Parte, related_name='seguimientos')
    cursoprofesor = models.ForeignKey(CursoProfesor)
    seguimiento = models.TextField(blank=False)

    def get_nombre_completo(self):

        return self.cursoprofesor.get_nombre_completo()

    class Meta:

        ordering = [ '-created' ]


