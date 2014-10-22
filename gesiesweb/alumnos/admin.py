from django.contrib import admin

from .models import Alumno

# Register your models here.

class AlumnoAdmin(admin.ModelAdmin):
	list_display = 	('nie', 'nombre', 'apellidos',
                         'fecha_nacimiento', 'foto_alumno')    

admin.site.register(Alumno, AlumnoAdmin)
