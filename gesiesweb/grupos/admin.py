# -*- encoding: utf-8 -*-

from django.contrib import admin

from .models import Grupo, CursoGrupo, GrupoAlumno, GrupoProfesor

class GrupoAdmin(admin.ModelAdmin):
    pass

class CursoGrupoAdmin(admin.ModelAdmin):
    list_filter = ('curso__curso',)

class GrupoAlumnoAdmin(admin.ModelAdmin):
    list_filter = ('cursogrupo__curso__curso',
                    'cursogrupo__grupo__grupo',)
    search_fields = ('cursoalumno__alumno__apellidos',)

class GrupoProfesorAdmin(admin.ModelAdmin):
    list_filter = ('cursogrupo__curso__curso',
                    'cursogrupo__grupo__grupo',
                    'cursoprofesor__profesor')
    search_fields = ('cursoprofesor__profesor__user__last_name',)

admin.site.register(Grupo, GrupoAdmin)
admin.site.register(CursoGrupo, CursoGrupoAdmin)
admin.site.register(GrupoAlumno, GrupoAlumnoAdmin)
admin.site.register(GrupoProfesor, GrupoProfesorAdmin)
