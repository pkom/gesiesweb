from django.db import models

from model_utils.models import TimeStampedModel

from config.models import Config
from cursos.models import Curso

class Rayuela(TimeStampedModel):
    TIPO = (
		('PR', 'Profesores'),
		('AL', 'Alumnos'),
    )
    curso = models.ForeignKey(Curso)
    tipo = models.CharField(max_length=2, choices=TIPO)
    archivo = models.FileField(upload_to='rayuela/%Y/%m/%d')
    procesado = models.BooleanField(default=False)
    resultado = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "%s %s [%s]" % (self.curso, self.TIPO[0 if self.tipo == 'PR' else 1][1], self.archivo)
