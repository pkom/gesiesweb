from django.db import models
from django.utils.encoding import smart_unicode

from cursos.models import Curso

# Create your models here.
class Config(models.Model):
    codigo_centro = models.CharField(unique=True, max_length=15)
    nombre_centro = models.CharField(unique=True, max_length=50)
    url_centro = models.URLField(max_length=200, blank=True)
    email_centro = models.EmailField(max_length=254, blank=True)
    direccion_centro = models.CharField(max_length=200, blank=True)
    telefono_centro = models.CharField(max_length=200, blank=True)
    fax_centro = models.CharField(max_length=200, blank=True)
    curso_academico_defecto = models.ForeignKey(Curso,
                                                blank=True, null=True,
                                                on_delete=models.SET_NULL)
    nombre_director = models.CharField(max_length=50, blank=True)
    firma_director = models.ImageField(upload_to='config', blank=True)
    logo_centro = models.ImageField(upload_to='config', blank=True)
    sello_centro = models.ImageField(upload_to='config', blank=True)

    def __unicode__(self):
    	return smart_unicode(self.nombre_centro)

    def logo(self):
        return """
        <img src ="%s"/>
        """ % self.logo_centro.url

    def sello(self):
        return """
        <img src ="%s"/>
        """ % self.sello_centro.url

    def firma(self):
        return """
        <img src ="%s"/>
        """ % self.firma_director.url

    logo.allow_tags = True
    sello.allow_tags = True
    firma.allow_tags = True

    # ordena por la funcion, no tiene sentido pero para documentar...
    logo.admin_order_field = 'nombre_centro'
