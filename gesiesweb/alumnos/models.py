from django.db import models
from model_utils.models import TimeStampedModel

class Alumno(TimeStampedModel):
    nie = models.CharField(unique=True, max_length=15)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    usuario_rayuela = models.CharField(max_length=20, blank=True)
    foto = models.ImageField(upload_to='alumnos', blank=True)

    def foto_alumno(self):
        return """
        <img src ="%s"/>
        """ % self.foto.url

    foto_alumno.allow_tags = True