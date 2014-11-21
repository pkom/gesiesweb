from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from core.mixins import LoginRequerido

from .models import Parte, ParteSeguimiento

class ParteListView(LoginRequerido, ListView):

    template_name = "partes/partes.html"
    model = Parte
    context_object_name = 'partes'

    def get_queryset(self):

        return Parte.objects.filter(cursoprofesor=self.request.session['curso_profesor'])

    def get_context_data(self, **kwargs):

        context = super(ParteListView, self).get_context_data(**kwargs)
        context['total_partes'] = Parte.objects.filter(cursoprofesor=self.request.session['curso_profesor']).count()
        context['total_partes_partes'] = Parte.objects.filter(cursoprofesor=self.request.session['curso_profesor'],
                                                              con_parte=True).count()
        context['total_partes_comunicados'] = Parte.objects.filter(cursoprofesor=self.request.session['curso_profesor'],
                                                              comunicado=True).count()
        context['total_partes_cerrados'] = Parte.objects.filter(cursoprofesor=self.request.session['curso_profesor'],
                                                              cerrado=True).count()
        return context


class ParteCreateView(LoginRequerido, CreateView):

    template_name = "partes/nuevo.html"
    model = Parte
    success_url = reverse_lazy('parte:partes')
    fields = ('fecha', 'parte', 'comunicado', )

    def form_valid(self, form):

        return super(ParteCreateView, self).form_valid(form)


    def form_invalid(self, form):

        return super(ParteCreateView, self).form_invalid(form)


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


    def get_context_data(self, **kwargs):

        context = super(ParteResponsableListView, self).get_context_data(**kwargs)
        context['total_partes'] = Parte.objects.filter(cursoprofesor__curso=self.request.session['curso_academico_usuario']).count()
        context['total_partes_partes'] = Parte.objects.filter(cursoprofesor__curso=self.request.session['curso_academico_usuario'],
                                                              con_parte=True).count()
        context['total_partes_comunicados'] = Parte.objects.filter(cursoprofesor__curso=self.request.session['curso_academico_usuario'],
                                                              comunicado=True).count()
        context['total_partes_cerrados'] = Parte.objects.filter(cursoprofesor__curso=self.request.session['curso_academico_usuario'],
                                                              cerrado=True).count()
        return context
