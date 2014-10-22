from django.contrib import admin

from .models import Config

# Register your models here.

class ConfigAdmin(admin.ModelAdmin):
	list_display = 	('codigo_centro', 'nombre_centro', 'nombre_director',
                         'logo', 'sello', 'firma')

	# para filtrar y que no salgan todo el contenido de la tabla en los foreigns
	# es recomendable establecer un search_field en la tabla relacionada para buscar
	# en ella
	#raw_id_fields = ('curso_academico_defecto',)

admin.site.register(Config, ConfigAdmin)
