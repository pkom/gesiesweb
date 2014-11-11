from django.db import models

from model_utils.models import TimeStampedModel

from django.utils.encoding import smart_unicode

# Create your models here.
class Curso(TimeStampedModel):
    curso = models.CharField(unique=True, max_length=9)
    retrasos_para_amonestacion = models.PositiveSmallIntegerField(default=2)
    retrasos_por_trimestres = models.BooleanField(default=True)
    inicio_trimestre_1 = models.DateField()
    fin_trimestre_1 = models.DateField()
    inicio_trimestre_2 = models.DateField()
    fin_trimestre_2 = models.DateField()
    inicio_trimestre_3 = models.DateField()
    fin_trimestre_3 = models.DateField()
    peso_1 = models.DecimalField(max_digits=5, decimal_places=2, default=100)
    peso_2 = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    peso_3 = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    peso_4 = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    peso_5 = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    peso_6 = models.DecimalField(max_digits=5, decimal_places=2, default=0)    

    def __unicode__(self):
    	return smart_unicode(self.curso)

    class Meta:
        ordering = [ 'curso' ]