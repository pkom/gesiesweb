#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from django.http.response import HttpResponse, HttpResponseBadRequest, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, DetailView, FormView

from braces.views import LoginRequiredMixin

from django.contrib.auth.models import User

from profesores.models import Profesor, CursoProfesor
from grupos.models import CursoGrupo, GrupoProfesor
from departamentos.models import DepartamentoProfesor, CursoDepartamento
from partes.models import Parte

from .forms import CourseAuthenticationForm

class HomeTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'core/index.html'

class LoginView(FormView):
    template_name = 'core/login.html'
    form_class = CourseAuthenticationForm
    #success_url = '/'

    def form_valid(self, form):
        login(self.request, form.user_cache)
        course = form.cleaned_data['course']
        fillsessionuser(self.request, form.user_cache, course)
        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
       # find your next url here
       next_url = self.request.POST.get('next',None) # here method should be GET or POST.
       if next_url:
           return "%s" % (next_url) # you can include some query strings as well
       else :
           return reverse('core:home') # what url you wish to return


@login_required
def mylogout(request):
    if request.user.is_authenticated():
        logout(request)
    return redirect('/core/login')


class AboutTemplateView(LoginRequiredMixin,TemplateView):

    template_name = 'core/about.html'


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class ProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = 'core/profile.html'
    model = User
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        usuario = Profesor.objects.get(user=context['user'])
        context['usuario'] = usuario
        context['ip'] = get_client_ip(self.request)
        context['partes'] = Parte.objects.filter(cursoprofesor=self.request.session['curso_profesor']).count()
        context['absentismos'] = 10
        context['retrasos'] = 2
        grupos = GrupoProfesor.objects.filter(cursogrupo__curso=self.request.session['curso_academico_usuario'],
                                              cursoprofesor=self.request.session['curso_profesor'])
        context['numgrupos'] = grupos.count()
        context['grupos'] = grupos
        context['asignaturas'] = 5
        context['alumnos'] = 135
        return context

@login_required
def updatename(request):
    if request.is_ajax():
        result = dict()
        if request.method == 'POST':
            user = User.objects.get(pk=request.POST['pk'])
            if request.POST['name'] == 'nombre':
                user.first_name = request.POST['value']
            elif request.POST['name'] == 'apellidos':
                user.last_name = request.POST['value']
            try:
                user.save()
            except:
                result['status'] = 'ERR'
                result['message'] = 'Error actualizando el dato'
                return HttpResponseBadRequest(json.dumps(result), content_type="application/json")
            result['status'] = 'OK'
            result['message'] = 'Dato actualizado'
            return HttpResponse(json.dumps(result), content_type="application/json")
        else:
            result['status'] = 'ERR'
            result['message'] = 'Petición errónea'
            return HttpResponseBadRequest(json.dumps(result), content_type="application/json")
    else:
        raise Http404


@login_required
def updatephoto(request):
    if request.is_ajax():
        result = dict()
        if request.method == 'POST':
            profesor = User.objects.get(pk=request.POST['pk']).profesor
            profesor.foto = request.FILES['avatar']
            try:
                profesor.save()
            except:
                result['status'] = 'ERR'
                result['message'] = 'Error al subir'
                return HttpResponseBadRequest(json.dumps(result), content_type="application/json")
            result['status'] = 'OK'
            result['message'] = 'Foto actualizada'
            result['url'] = profesor.foto.url
            return HttpResponse(json.dumps(result), content_type="application/json")
        else:
            result['status'] = 'ERR'
            result['message'] = 'Petición errónea'
            return HttpResponseBadRequest(json.dumps(result), content_type="application/json")
    else:
        raise Http404



def fillsessionuser(request, user, course):
    request.session['curso_academico_usuario'] = course
    cursoprofesor, created = CursoProfesor.objects.get_or_create(curso=course,profesor=user.profesor)
    request.session['curso_profesor'] = cursoprofesor
    request.session['es_responsable'] = cursoprofesor.es_responsable
    try:
        cursogrupo = CursoGrupo.objects.get(curso=course,tutor=cursoprofesor)
    except ObjectDoesNotExist:
        request.session['es_tutor'] = False
    else:
        request.session['es_tutor'] = True
        request.session['grupo_tutoria'] = cursogrupo
    try:
        departamentoprofesor = DepartamentoProfesor.objects.get(cursodepartamento__curso=course, cursoprofesor=cursoprofesor)
    except ObjectDoesNotExist:
        request.session['departamento_profesor'] = 'Sin Departamento Asignado'
    else:
        request.session['departamento_profesor'] = departamentoprofesor
    try:
        cursodepartamento = CursoDepartamento.objects.get(curso=course, jefe=cursoprofesor)
    except ObjectDoesNotExist:
        request.session['es_jefe'] = False
    else:
        request.session['es_jefe'] = True
        request.session['curso_departamento'] = cursodepartamento
    request.session['grupos_asignaturas_alumnos'] = [dict(id=1, grupo="2AE", asignatura=dict(id=1, asignatura="Matemáticas",
                                                                                             abreviatura="MAT"),
                                                          alumnos=[dict(id=1, apellidos="Moreno Jiménez", nombre="Alberto",
                                                                        foto='avatars/profile-pic.jpg'),
                                                                   dict(id=2, apellidos="Sánchez Jiménez", nombre="Lorena",
                                                                        foto='avatars/profile-pic.jpg')
                                                                   ]),
                                                     dict(id=2, grupo="2BE", asignatura=dict(id=2, asignatura="Destreza Básica de Matemáticas",
                                                                                             abreviatura="DBM"),
                                                          alumnos=[dict(id=3, apellidos="González Barrantes", nombre="Francisco",
                                                                        foto='avatars/profile-pic.jpg'),
                                                                   dict(id=4, apellidos="Ruíz Calero", nombre="Antonia",
                                                                        foto='avatars/profile-pic.jpg')
                                                                   ])
                                                     ]