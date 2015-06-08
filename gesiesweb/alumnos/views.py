# -*- coding: utf-8 -*-

from django.db.models import Q
from django.http import JsonResponse, HttpResponseForbidden, HttpResponseNotAllowed, HttpResponseServerError
from django.views.generic import ListView

from rest_framework import viewsets

from .models import Alumno
from grupos.models import GrupoAlumno


# Create your views here.
class ConfigListView(ListView):
    model = Alumno
    context_object_name = 'alumnos'
    template_name = 'alumnos/alumnos.html'

def dame_alumnos_curso(request):
    if request.user.is_authenticated():
        if request.method == 'GET':
            id_grupo = request.GET.get('idgrupo', '')
            try:
                if id_grupo:
                    grupoalumnos = GrupoAlumno.objects.filter(cursogrupo__curso=request.session['curso_academico_usuario'],
                                                          cursogrupo_id=id_grupo)
                else:
                    grupoalumnos = GrupoAlumno.objects.filter(cursogrupo__curso=request.session['curso_academico_usuario'])
            except Exception:
                return HttpResponseServerError({"estado": "fallo",
                                                "error": "Ha ocurrido un error al procesar la petición en el servidor",
                                                "descripcion": Exception.message})
            result = []
            for alumno in grupoalumnos:
                result.append({'id': alumno.id,
                               #'foto': alumno.cursoalumno.get_foto(),
                               'nombre': alumno.cursoalumno.get_nombre_completo()})
            return JsonResponse(result, safe=False)
        else:
            return HttpResponseNotAllowed({"estado": "fallo",
                                           "error": "No tienes permiso para realizar esta acción"})
    else:
        return HttpResponseForbidden({"estado": "fallo",
                                      "error": "No has hecho login o la sesión ha caducado"})
