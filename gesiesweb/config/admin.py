from django.contrib import admin

from .models import Config

# Register your models here.

class ConfigAdmin(admin.ModelAdmin):
	list_display = 	('codigo_centro', 'nombre_centro', 'nombre_director',
                         'logo', 'sello', 'firma')

admin.site.register(Config, ConfigAdmin)
