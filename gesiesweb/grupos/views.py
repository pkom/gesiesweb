# -*- coding: utf-8 -*-
from django.http import JsonResponse, HttpResponseForbidden, HttpResponseNotAllowed, HttpResponseServerError

from .models import CursoGrupo

# Create your views here.

def dame_grupos_curso(request):
    if request.user.is_authenticated():
        if request.method == 'GET':
            try:
                cursogrupos = CursoGrupo.objects.filter(curso=request.session['curso_academico_usuario'])
            except Exception:
                return HttpResponseServerError({"estado": "fallo",
                                                "error": "Ha ocurrido un error al procesar la petición en el servidor",
                                                "descripcion": Exception.message})
            result = []
            for grupo in cursogrupos:
                result.append({'id': grupo.id,
                               'grupo': grupo.grupo.grupo})
            return JsonResponse(result, safe=False)
        else:
            return HttpResponseNotAllowed({"estado": "fallo",
                                           "error": "No tienes permiso para realizar esta acción"})
    else:
        return HttpResponseForbidden({"estado": "fallo",
                                      "error": "No has hecho login o la sesión ha caducado"})