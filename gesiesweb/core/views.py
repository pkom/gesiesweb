#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.views.generic import TemplateView, DetailView, FormView

from braces.views import LoginRequiredMixin

from django.contrib.auth.models import User

from .forms import CourseAuthenticationForm
from usuarios.models import Usuario

class HomeTemplateView(LoginRequiredMixin, TemplateView):

    template_name = 'core/index.html'

class LoginView(FormView):
    template_name = 'core/login.html'
    form_class = CourseAuthenticationForm
    success_url = '/'

    def form_valid(self, form):

        login(self.request, form.user_cache)
        course = form.cleaned_data['course']
        fillsessionuser(self.request, form.user_cache, course)
        return super(LoginView, self).form_valid(form)


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
        usuario = Usuario.objects.get(user=context['user'])
        context['usuario'] = usuario
        context['ip'] = get_client_ip(self.request)
        context['partes'] = 23
        context['absentismos'] = 10
        context['retrasos'] = 2
        context['grupos'] = 14
        context['asignaturas'] = 5
        context['alumnos'] = 135
        return context

@login_required
def postprofile(request):
    print "Es ajax "+request.is_ajax()
    if request.method == 'POST':
        print request.POST['value']
        print request.POST['name']
        print request.POST['pk']

def fillsessionuser(request, user, course):
    request.session['curso_academico_usuario'] = course
    request.session['es_responsable'] = True
    request.session['es_tutor'] = True
    request.session['es_jefe'] = True
    request.session['grupo_tutoria'] = dict(id=1, grupo='2AE')
    request.session['departamento'] = dict(id=1, departamento='Matemáticas')
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