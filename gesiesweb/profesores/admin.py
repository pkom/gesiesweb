from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from sorl.thumbnail.admin import AdminImageMixin

from profesores.models import Profesor, CursoProfesor


class ProfesorAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('user_full_name', 'dni', 'usuario_rayuela', 'foto', 'es_usuario', 'id_usuario')

    def user_full_name(self, obj):
        return (u'%s, %s' % (obj.user.last_name, obj.user.first_name))

    user_full_name.short_description = u'Profesor'


class CursoProfesorAdmin(admin.ModelAdmin):
    list_display = ('curso', 'profesor',)
    ordering = ('profesor__user__last_name',)
    list_filter = ('curso__curso',)

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