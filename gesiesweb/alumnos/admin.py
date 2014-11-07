from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from .models import Alumno, CursoAlumno

class AlumnoAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = 	('nie', 'nombre', 'apellidos', 'fecha_nacimiento', 'foto',)
    ordering = ('apellidos','nombre',)
    search_fields = ('apellidos', 'nombre',)

class CursoAlumnoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'alumno',)
    ordering = ('alumno__apellidos','alumno__nombre',)
    list_filter = ('curso__curso',)

admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(CursoAlumno, CursoAlumnoAdmin)