from django.contrib import admin

from .models import Grupo, CursoGrupo, GrupoAlumno, GrupoProfesor

class GrupoAdmin(admin.ModelAdmin):
    pass

class CursoGrupoAdmin(admin.ModelAdmin):
    pass

class GrupoAlumnoAdmin(admin.ModelAdmin):
    pass

class GrupoProfesorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Grupo, GrupoAdmin)
admin.site.register(CursoGrupo, CursoGrupoAdmin)
admin.site.register(GrupoAlumno, GrupoAlumnoAdmin)
admin.site.register(GrupoProfesor, GrupoProfesorAdmin)
