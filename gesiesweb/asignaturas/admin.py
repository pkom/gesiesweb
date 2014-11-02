from django.contrib import admin

from .models import Asignatura, DepartamentoAsignatura

class AsignaturaAdmin(admin.ModelAdmin):
    pass

class DepartamentoAsignaturaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Asignatura, AsignaturaAdmin)
admin.site.register(DepartamentoAsignatura, DepartamentoAsignaturaAdmin)