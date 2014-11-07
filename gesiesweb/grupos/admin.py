# -*- encoding: utf-8 -*-

from django.contrib import admin

from .models import Grupo, CursoGrupo, GrupoAlumno, GrupoProfesor

class GrupoAdmin(admin.ModelAdmin):
    ordering = ('grupo',)

class CursoGrupoAdmin(admin.ModelAdmin):
    ordering = ('grupo__grupo',)
    list_filter = ('curso__curso',)

class GrupoAlumnoAdmin(admin.ModelAdmin):
    ordering = ('cursogrupo__grupo__grupo','cursoalumno__alumno__apellidos','cursoalumno__alumno__nombre',)
    list_filter = ('cursogrupo__curso__curso',
                    'cursogrupo__grupo__grupo',)
#                    'cursoalumno__alumno')
    search_fields = ('cursoalumno__alumno__apellidos',)

class GrupoProfesorAdmin(admin.ModelAdmin):
    ordering = ('cursogrupo__grupo__grupo',)
    list_filter = ('cursogrupo__curso__curso',
                    'cursogrupo__grupo__grupo',
                    'cursoprofesor__profesor')
    search_fields = ('cursoprofesor__profesor__user__last_name',)

admin.site.register(Grupo, GrupoAdmin)
admin.site.register(CursoGrupo, CursoGrupoAdmin)
admin.site.register(GrupoAlumno, GrupoAlumnoAdmin)
admin.site.register(GrupoProfesor, GrupoProfesorAdmin)
