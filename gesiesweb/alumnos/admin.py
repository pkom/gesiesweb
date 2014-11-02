from django.contrib import admin

from .models import Alumno, CursoAlumno

class AlumnoAdmin(admin.ModelAdmin):
	list_display = 	('nie', 'nombre', 'apellidos',
                         'fecha_nacimiento', 'foto_alumno')    

class CursoAlumnoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(CursoAlumno, CursoAlumnoAdmin)