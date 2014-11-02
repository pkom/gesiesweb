from django.contrib import admin

from .models import Departamento, CursoDepartamento, DepartamentoProfesor

class DepartamentoAdmin(admin.ModelAdmin):
    pass

class CursoDepartamentoAdmin(admin.ModelAdmin):
    pass

class DepartamentoProfesorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(CursoDepartamento, CursoDepartamentoAdmin)
admin.site.register(DepartamentoProfesor, DepartamentoProfesorAdmin)
