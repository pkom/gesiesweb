# -*- coding: utf-8 -*-

from django.db.models import Q
from django.http import JsonResponse, HttpResponseForbidden, HttpResponseNotAllowed, HttpResponseServerError
from django.views.generic import ListView

from rest_framework import viewsets

from .models import Alumno, CursoAlumno


# Create your views here.
class ConfigListView(ListView):
    model = Alumno
    context_object_name = 'alumnos'
    template_name = 'alumnos/alumnos.html'

def dame_alumnos_curso(request):
    if request.user.is_authenticated():
        if request.method == 'GET':
            term = request.GET.get('term', '')
            if term:
                try:
                    cursoalumnos = CursoAlumno.objects.filter(Q(alumno__nombre__icontains=term)
                                                              | Q(alumno__apellidos__icontains=term),
                                                              curso=request.session['curso_academico_usuario'])
                except Exception:
                    return HttpResponseServerError({"estado": "fallo",
                                                    "error": "Ha ocurrido un error al procesar la petición en el servidor",
                                                    "descripcion": Exception.message})
                result = []
                for alumno in cursoalumnos:
                    result.append({'id': alumno.id,
                                   'foto': alumno.get_foto(),
                                   'nombre': alumno.get_nombre_completo()})
                return JsonResponse(result, safe=False)
            else:
                return HttpResponseServerError("Error: No se ha recibido el valor a buscar")
        else:
            return HttpResponseNotAllowed({"estado": "fallo",
                                           "error": "No tienes permiso para realizar esta acción"})
    else:
        return HttpResponseForbidden({"estado": "fallo",
                                      "error": "No has hecho login o la sesión ha caducado"})
