from django.contrib import admin

from .models import Departamento, CursoDepartamento, DepartamentoProfesor


class DepartamentoAdmin(admin.ModelAdmin):

    pass


class CursoDepartamentoAdmin(admin.ModelAdmin):

    list_filter = ('curso__curso',)


class DepartamentoProfesorAdmin(admin.ModelAdmin):

    list_filter = ('cursodepartamento__curso__curso',
                   'cursodepartamento__departamento__departamento',
                    'cursoprofesor__profesor')
    search_fields = ('cursoprofesor__profesor__user__last_name',)


admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(CursoDepartamento, CursoDepartamentoAdmin)
admin.site.register(DepartamentoProfesor, DepartamentoProfesorAdmin)
