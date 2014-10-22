from django.db import models

class Rayuela(models.Model):
    TIPO = (
		('PRO', 'Profesores'),
		('ALU', 'Alumnos'),
    )
    tipo = models.CharField(max_length=2, choices=TIPO)
    archivo = models.FileField(upload_to='rayuela')
    procesado = models.BooleanField(default=False)
    resultado = models.TextField()
