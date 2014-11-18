from django.views.generic import ListView, DetailView

from core.mixins import LoginRequerido

from .models import Parte, ParteSeguimiento

class PartesListView(LoginRequerido, ListView):

    template_name = "partes/partes.html"
    model = Parte
    context_object_name = 'partes'

    def get_queryset(self):

        return Parte.objects.filter(cursoprofesor=self.request.session['curso_profesor'])


class PartesResponsableListView(LoginRequerido, ListView):

    template_name = "partes/partes_responsables.html"
    model = Parte
    context_object_name = 'partes'

    def get_queryset(self):

        return Parte.objects.filter(cursoprofesor__curso=self.request.session['curso_academico_usuario'])


class PartesDetailView(LoginRequerido, DetailView):

    template_name = "partes/detalle.html"
    model = Parte
    context_object_name = 'parte'
