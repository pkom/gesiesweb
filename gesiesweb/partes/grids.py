# -*- coding: utf-8 -*-

import json

from django.http import JsonResponse, HttpResponseForbidden, HttpResponseNotAllowed, HttpResponseServerError
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy
#imports para la paginacion
from django.core.paginator import Paginator, InvalidPage, EmptyPage


from api.serializers import ParteSerializer
from core.jqgrid import JqGrid

from grupos.models import GrupoAlumno
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


def partes_profesor(request):
    if request.user.is_authenticated():
        if request.method == 'GET':
            page = request.GET.get('page', '')
            limit = request.GET.get('rows', '')
            sidx = request.GET.get('sidx', '')
            sord = request.GET.get('sord', '')
            busqueda = request.GET.get('_search','')

            if sord == 'asc':
                sord = ''
            elif sord == 'desc':
                sord = '-'

            partes = Parte.objects.filter(cursoprofesor__id=request.session['curso_profesor'].id)

            if busqueda == 'true':
                filter_map = {
                    # jqgrid op: (django_lookup, use_exclude)
                    'ne': ('%(field)s__exact', True),
                    'bn': ('%(field)s__startswith', True),
                    'en': ('%(field)s__endswith', True),
                    'nc': ('%(field)s__contains', True),
                    'ni': ('%(field)s__in', True),
                    'in': ('%(field)s__in', False),
                    'eq': ('%(field)s__exact', False),
                    'bw': ('%(field)s__startswith', False),
                    'gt': ('%(field)s__gt', False),
                    'ge': ('%(field)s__gte', False),
                    'lt': ('%(field)s__lt', False),
                    'le': ('%(field)s__lte', False),
                    'ew': ('%(field)s__endswith', False),
                    'cn': ('%(field)s__contains', False)
                }
                _filters = request.GET.get('filters')
                try:
                    filters = _filters and json.loads(_filters)
                except ValueError:
                    filters = None

                if filters:
                    for rule in filters['rules']:
                        op, field, data = rule['op'], rule['field'], rule['data']
                        if field == "alumno":
                            partes = partes.filter(Q(grupoalumno__cursoalumno__alumno__nombre__icontains=data) |
                                               Q(grupoalumno__cursoalumno__alumno__apellidos__icontains=data))
                        if field == "grupo":
                            partes = partes.filter(grupoalumno__cursogrupo_id=data)
                        if field == "fecha":
                            partes = partes.filter(fecha__range=[data, "9999-12-31"])
                        if field == "con_parte":
                            partes = partes.filter(con_parte=True if data == 'True' else False)
                        if field == "comunicado":
                            partes = partes.filter(comunicado=True if data == 'True' else False)
                        if field == "cerrado":
                            partes = partes.filter(cerrado=True if data == 'True' else False)

                else:
                    if request.GET.get('grupo'):
                        grupo = request.GET.get('grupo')
                        partes = partes.filter(grupoalumno__cursogrupo__grupo__grupo__contains=grupo)
                    if request.GET.get('alumno'):
                        nombre = request.GET.get('alumno')
                        partes = partes.filter(Q(grupoalumno__cursoalumno__alumno__nombre__icontains=nombre) |
                                               Q(grupoalumno__cursoalumno__alumno__apellidos__icontains=nombre))
                    if request.GET.get('fecha'):
                        fecha = request.GET.get('fecha')
                        #fechafield = datetime.strptime(fecha, '%Y-%m-%d')
                        #partes = partes.filter(fecha__ge=fechafield)
                        partes = partes.filter(fecha__range=[fecha, "9999-12-31"])
                    if request.GET.get('con_parte'):
                        con_parte = request.GET.get('con_parte')
                        if con_parte == 'True':
                            partes = partes.filter(con_parte=True)
                        else:
                            partes = partes.filter(con_parte=False)
                    if request.GET.get('comunicado'):
                        comunicado = request.GET.get('comunicado')
                        if comunicado == 'True':
                            partes = partes.filter(comunicado=True)
                        else:
                            partes = partes.filter(comunicado=False)
                    if request.GET.get('cerrado'):
                        cerrado = request.GET.get('cerrado')
                        if cerrado == 'True':
                            partes = partes.filter(cerrado=True)
                        else:
                            partes = partes.filter(cerrado=False)

            if str(sidx) == "grupo":
                partes = partes.order_by(str(sord) + str("grupoalumno__cursogrupo__grupo__grupo"), '-fecha', '-id')
            elif str(sidx) == "alumno":
                partes = partes.order_by(str(sord) + str("grupoalumno__cursoalumno__alumno__apellidos"),
                                         str("grupoalumno__cursoalumno__alumno__nombre"),
                                         '-fecha', '-id')
            else:
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
                        "parte": r.parte,
                        "id_grupoalumno": r.grupoalumno.id,
                        "id_cursogrupo": r.grupoalumno.cursogrupo.id}
                filas.append(fila)
                i += 1
            results = {"page": page, "total": paginator.num_pages, "records": n_partes, "rows": filas}
            #return JsonResponse(json_encode(results), safe=False)
            return JsonResponse(results, safe=False)
        else:
            return HttpResponseNotAllowed({"estado": "fallo",
                                           "error": "No tienes permiso para realizar esta acción"})
    else:
        return HttpResponseForbidden({"estado": "fallo",
                                      "error": "No has hecho login o la sesión ha caducado"})

def partes_actualiza(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            oper = request.POST.get('oper', '')
            if oper == "add":
                #añadimos nuevo parte
                parte = Parte()
                parte.cursoprofesor = request.session['curso_profesor']
                idalumno = request.POST.get('alumno', '')
                if not idalumno:
                    results = {"estado": "fallo", "error": "No se ha seleccionado un alumn@"}
                    return JsonResponse(results, safe=False)
                try:
                    alumno = GrupoAlumno.objects.get(id=idalumno)
                except GrupoAlumno.DoesNotExist:
                    results = {"estado": "fallo", "error": "No se ha podido localizar el alumno"}
                    return JsonResponse(results, safe=False)
                parte.grupoalumno = alumno
                parte.fecha = request.POST.get('fecha', '')
                parte.parte = request.POST.get('parte', '')
                parte.comunicado = request.POST.get('comunicado', '')
            elif oper == "edit":
                #modificamos un parte
                idparte = request.POST.get('id', '')
                if not idparte:
                    results = {"estado": "fallo", "error": "No se ha seleccionado un parte"}
                    return JsonResponse(results, safe=False)
                try:
                    parte = Parte.objects.get(id=idparte)
                except Parte.DoesNotExist:
                    results = {"estado": "fallo", "error": "No se ha podido localizar el parte"}
                    return JsonResponse(results, safe=False)
                if request.session['curso_profesor'] == parte.cursoprofesor or request.session['es_responsable']:
                    idalumno = request.POST.get('alumno', '')
                    if not idalumno:
                        results = {"estado": "fallo", "error": "No se ha seleccionado un alumn@"}
                        return JsonResponse(results, safe=False)
                    try:
                        alumno = GrupoAlumno.objects.get(id=idalumno)
                    except GrupoAlumno.DoesNotExist:
                        results = {"estado": "fallo", "error": "No se ha podido localizar el alumno"}
                        return JsonResponse(results, safe=False)
                    parte.grupoalumno = alumno
                    parte.fecha = request.POST.get('fecha', '')
                    parte.parte = request.POST.get('parte', '')
                    parte.comunicado = request.POST.get('comunicado', '')
                else:
                    return HttpResponseNotAllowed({"estado": "fallo",
                                                   "error": "No tienes permiso para realizar esta acción"})
            else:
                id = request.POST.get('id', '')
                campo = request.POST.get('campo', '')
                isChecked = request.POST.get('isChecked', '')
                parte = Parte.objects.get(id=id)
                if campo == 'comunicado':
                    parte.comunicado = True if isChecked == "true" else False
                elif campo == 'con_parte':
                    parte.con_parte = True if isChecked == "true" else False
                elif campo == 'cerrado':
                    parte.cerrado = True if isChecked == "true" else False

            try:
                parte.save()
            except Exception:
                return HttpResponseServerError(Exception.message)
            results = {"estado": "ok",
                       "parte": ParteSerializer(parte).data}
            return JsonResponse(results, safe=False)
        else:
            return HttpResponseNotAllowed({"estado": "fallo",
                                           "error": "No tienes permiso para realizar esta acción"})
    else:
        return HttpResponseForbidden({"estado": "fallo",
                                      "error": "No has hecho login o la sesión ha caducado"})
