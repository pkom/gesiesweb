from django.db import models

from model_utils.models import TimeStampedModel

from departamentos.models import Departamento

class Asignatura(TimeStampedModel):
    abreviatura = models.CharField(max_length=20, db_index=True)
    asignatura = models.CharField(max_length=60)

    def __unicode__(self):
        return "%s - %s" % (self.abreviatura, self.asignatura)

class DepartamentoAsignatura(TimeStampedModel):
    departamento = models.ForeignKey(Departamento)
    asignatura = models.ForeignKey(Asignatura)

    def __unicode__(self):
        return "%s - %s" % (self.departamento, self.asignatura)

    class Meta:
        unique_together = (("departamento", "asignatura"),)