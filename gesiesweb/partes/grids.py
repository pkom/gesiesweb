from django.core.urlresolvers import reverse_lazy

from core.jqgrid import JqGrid

from partes.models import Parte

class ParteGrid(JqGrid):
    model = Parte
    fields = ['id', 'grupoalumno__cursogrupo__grupo__descripcion', 'grupoalumno__cursoalumno__alumno__apellidos',
              'fecha', 'con_parte', 'comunicado', 'cerrado']
    url = reverse_lazy('parte:grid_handler')
    caption = 'Partes del Profesor'
    pager_id = '#pager'
    colmodel_overrides = {
        'id': { 'label': 'Id', 'width': 10, 'align': 'right', 'editable': 'false' },
        'grupoalumno__cursogrupo__grupo__descripcion': { 'label': 'Grupo', 'width': 10, 'align': 'center'},
        'grupoalumno__cursoalumno__alumno__apellidos': { 'label': 'Alumn@' },
        'fecha': {'label': 'Fecha', 'width': 20, 'align': 'center'},
        'con_parte': {'label': 'Parte', 'width': 20, 'align': 'center', 'formatter': 'checkbox', 'editable': 'false'},
        'comunicado': {'label': 'Comunicado', 'width': 20, 'align': 'center', 'formatter': 'checkbox',
                       'formatoptions': {'disabled': 'false'}},
        'cerrado': {'label': 'Cerrado', 'width': 20, 'align': 'center', 'formatter': 'checkbox', 'editable': 'false'}
    }

class ParteGridResponsable(JqGrid):
    model = Parte
    fields = ['id', 'grupoalumno_id', 'cursoprofesor_id', 'fecha', 'con_parte', 'comunicado', 'cerrado'] # optional
    url = reverse_lazy('parte:grid_handler_responsable')
    caption = 'Partes del Centro'
    pager_id = '#pager_responsable'
    colmodel_overrides = {
        'id': { 'editable': False, 'width': 20, 'align': 'right' },
    }