from django.contrib import admin

from .models import Parte, ParteSeguimiento


class ParteSeguimientoInline(admin.StackedInline):

    model = ParteSeguimiento
    list_display = ( 'id', 'cursoprofesor', 'seguimiento', 'created', 'modified', )
    extra = 1
    readonly = ( 'created', 'modified', )


class ParteAdmin(admin.ModelAdmin):

    list_display = ( 'id', 'cursoalumno', 'cursoprofesor', 'fecha', 'parte', 'con_parte', 'comunicado',
                     'cerrado', 'created', 'modified', )
    readonly = ( 'created', 'modified', )
    inlines = [ ParteSeguimientoInline ]
    list_filter = ('cursoalumno__curso__curso',
                    'con_parte',
                    'comunicado',
                    'cerrado',
#                   'cursoalumno__alumno',
                    'cursoprofesor__profesor', )

admin.site.register(Parte, ParteAdmin)
