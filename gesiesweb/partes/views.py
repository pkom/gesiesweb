from django.views.generic import ListView, CreateView, DetailView

from core.mixins import LoginRequerido

from .models import Parte, ParteSeguimiento

class ParteListView(LoginRequerido, ListView):

    template_name = "partes/partes.html"
    model = Parte
    context_object_name = 'partes'

    def get_queryset(self):

        return Parte.objects.filter(cursoprofesor=self.request.session['curso_profesor'])


class ParteCreateView(LoginRequerido, CreateView):

    pass


class ParteDetailView(LoginRequerido, DetailView):

    template_name = "partes/detalle.html"
    model = Parte
    context_object_name = 'parte'


class ParteUpdateView(LoginRequerido, DetailView):

    pass


class ParteDeleteView(LoginRequerido, DetailView):

    pass


class ParteResponsableListView(LoginRequerido, ListView):

    template_name = "partes/partes_responsables.html"
    model = Parte
    context_object_name = 'partes'

    def get_queryset(self):

        return Parte.objects.filter(cursoprofesor__curso=self.request.session['curso_academico_usuario'])


