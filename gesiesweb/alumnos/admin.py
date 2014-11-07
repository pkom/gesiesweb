from django.contrib import admin

from .models import Alumno, CursoAlumno

class AlumnoAdmin(admin.ModelAdmin):
    list_display = 	('nie', 'nombre', 'apellidos', 'fecha_nacimiento', 'foto_alumno')
    ordering = ('apellidos','nombre',)

class CursoAlumnoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'alumno',)
    ordering = ('alumno__apellidos','alumno__nombre',)
    list_filter = ('curso__curso',)

admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(CursoAlumno, CursoAlumnoAdmin)