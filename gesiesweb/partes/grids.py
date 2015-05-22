from django.core.urlresolvers import reverse_lazy
#imports para la paginacion
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponseRedirect, HttpResponse
import json

from core.jqgrid import JqGrid

from partes.models import Parte

class ParteGrid(JqGrid):
    model = Parte
    def get_queryset(self, request):
        return Parte.objects.filter(cursoprofesor__id=request.session['curso_profesor'].id).order_by('-fecha', 'id')

    fields = ['id', 'grupoalumno__cursogrupo__grupo__grupo', 'grupoalumno__cursoalumno__alumno__foto',
              'grupoalumno__cursoalumno__alumno__apellidos', 'fecha', 'con_parte', 'comunicado', 'cerrado', 'parte']

    #url = reverse_lazy('parte:grid_handler')
    url = reverse_lazy('parte:grid_profesor_data')
    caption = 'Partes del Profesor'
    pager_id = '#pager'
    colmodel_overrides = {
        'id': { 'label': 'Id', 'hidden': True, 'editable': False, 'sortable': False, 'search': False},
        'grupoalumno__cursogrupo__grupo__grupo': {'name': 'grupoalumno__cursogrupo__grupo__grupo',
                                                  'index':'grupoalumno__cursogrupo__grupo__grupo',
                                                  'label': 'Grupo', 'width': 10, 'align': 'center',
                                                  'searchOptions': {'attr':'Introduce grupo:', 'sopt':['cn'],
                                                                    'clearSearch':True}},
        'grupoalumno__cursoalumno__alumno__foto': {'index': 'grupoalumno__cursoalumno__alumno__foto', 'search': False,
                                                   'label': 'Foto', 'width': 10, 'align': 'center', 'sortable':False},
        'grupoalumno__cursoalumno__alumno__apellidos': {'index': 'grupoalumno__cursoalumno__alumno__apellidos',
                                                        'label': 'Alumn@'},
        'fecha': {'label': 'Fecha', 'width': 15, 'align': 'center', 'search': True},
        'con_parte': {'label': 'Parte', 'width': 15, 'align': 'center', 'formatter': 'checkbox', 'editable': False,
                      'sortable': False, 'search': False},
        'comunicado': {'label': 'Comunicado', 'width': 15, 'align': 'center', 'formatter': 'checkbox',
                       'formatoptions': {'disabled': False}, 'sortable': False, 'search': False},
        'cerrado': {'label': 'Cerrado', 'width': 15, 'align': 'center', 'formatter': 'checkbox', 'editable': False,
                    'sortable': False, 'search': False},
        'parte': { 'label': 'Parte', 'hidden': True, 'editable': True, 'sortable': False, 'search': False}
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


from django.core.serializers.json import DjangoJSONEncoder
def json_encode(data):
    encoder = DjangoJSONEncoder()
    return encoder.encode(data)


def ver_jqgrid_partes_profesor(request):
    if request.user.is_authenticated() and request.method == 'GET':
        page = request.GET.get('page', '')
        limit = request.GET.get('rows', '')
        sidx = request.GET.get('sidx', '')
        sord = request.GET.get('sord', '')
        busqueda = request.GET.get('_search','')

        if sord == 'asc':
            sord = '-'
        elif sord == 'desc':
            sord = ''

        partes = Parte.objects.filter(cursoprofesor__id=request.session['curso_profesor'].id)

        if busqueda == 'true':
            campo = request.GET.get('searchField','')
            operacion = request.GET.get('searchOper','')
            palabra = request.GET.get('searchString','')

            if campo == 'grupo':
                if operacion == "eq":
                    students = partes.filter(grupoalumno__cursogrupo__grupo__grupo__exact=palabra)
                elif operacion == "nq":
                    students = partes.exclude(grupoalumno__cursogrupo__grupo__grupo__exact=palabra)
                elif operacion == "bw":
                    students = partes.filter(grupoalumno__cursogrupo__grupo__grupo__startswith=palabra)
                elif operacion == "bn":
                    students = partes.exclude(grupoalumno__cursogrupo__grupo__grupo__startswith=palabra)
                elif operacion == "ew":
                    students = partes.filter(grupoalumno__cursogrupo__grupo__grupo__endswith=palabra)
                elif operacion == "en":
                    students = partes.exclude(grupoalumno__cursogrupo__grupo__grupo__endswith=palabra)
                elif operacion == "cn":
                    students = partes.filter(grupoalumno__cursogrupo__grupo__grupo__contains=palabra)
                elif operacion == "nc":
                    students = partes.exclude(grupoalumno__cursogrupo__grupo__grupo__contains=palabra)

        partes = partes.order_by(str(sord) + str(sidx), '-id')

        n_partes = partes.count()
        paginator = Paginator(partes, int(limit))

        try:
            page = request.GET.get('page', '1')
        except ValueError:
            page = 1

        try:
            resultados = paginator.page(page)
        except (EmptyPage, InvalidPage):
            resultados = paginator.page(paginator.num_pages)

        filas = []
        i = 1
        for r in resultados.object_list:
            fila = {"id": r.id,
                    "grupo": r.grupoalumno.cursogrupo.grupo.grupo,
                    "foto": r.get_foto_alumno_peque(),
                    "alumno": r.get_nombre_completo_alumno(),
                    "fecha": r.fecha,
                    "con_parte": r.con_parte,
                    "comunicado": r.comunicado,
                    "cerrado": r.cerrado,
                    "parte": r.parte}
            filas.append(fila)
            i += 1
        results = {"page": page, "total": paginator.num_pages, "records": n_partes, "rows": filas}
        #return HttpResponse(simplejson.dumps(results, indent=4), mimetype='application/json')
        return HttpResponse(
            json_encode(results),
            content_type="application/json"
        )
