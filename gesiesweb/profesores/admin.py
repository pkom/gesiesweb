from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from profesores.models import Profesor, CursoProfesor

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('user', 'dni', 'usuario_rayuela', 'foto', 'es_usuario', 'id_usuario')

class CursoProfesorAdmin(admin.ModelAdmin):
    pass

class ProfesorInline(admin.StackedInline):
    model = Profesor
    can_delete = False
    verbose_name_plural = 'profesor'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ProfesorInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(CursoProfesor, CursoProfesorAdmin)