from django.contrib import admin

from .models import Curso

# Register your models here.

class CursoAdmin(admin.ModelAdmin):
	list_display = ('curso', 'retrasos_para_amonestacion', 'retrasos_por_trimestres',
		    		'peso_1', 'peso_2', 'peso_3', 'peso_4', 'peso_5', 'peso_6')
	list_filter = ('curso', )
	search_fields = ('curso', )
	list_editable = ('retrasos_para_amonestacion', 'retrasos_por_trimestres')
	# podemos pasar acciones a ejecutar, pasando el nombre de la funcion definida
	# en actions.py o en otro sitio
	#actions = (procesa_curso, )

admin.site.register(Curso, CursoAdmin)
