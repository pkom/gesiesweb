from django.core.urlresolvers import reverse_lazy

from core.jqgrid import JqGrid

from partes.models import Parte

class ParteGrid(JqGrid):
    model = Parte
    fields = ['id', 'grupoalumno_id', 'cursoprofesor_id', 'fecha', 'con_parte', 'comunicado', 'cerrado'] # optional
    url = reverse_lazy('parte:grid_handler')
    caption = 'Partes del Centro'
#    colmodel_overrides = {
#        'id': { 'editable': False, 'width':10 },
#    }