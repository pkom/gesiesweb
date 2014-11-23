from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from django_datatables_view.base_datatable_view import BaseDatatableView

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
        context['total_partes'] = Parte.objects.filter(
            cursoprofesor__curso=self.request.session['curso_academico_usuario']).count()
        context['total_partes_partes'] = Parte.objects.filter(
            cursoprofesor__curso=self.request.session['curso_academico_usuario'],
            con_parte=True).count()
        context['total_partes_comunicados'] = Parte.objects.filter(
            cursoprofesor__curso=self.request.session['curso_academico_usuario'],
            comunicado=True).count()
        context['total_partes_cerrados'] = Parte.objects.filter(
            cursoprofesor__curso=self.request.session['curso_academico_usuario'],
            cerrado=True).count()
        return context


class ParteResponsableBaseDatatableView(LoginRequerido, BaseDatatableView):
    model = Parte
    columns = ['id', 'fecha', 'grupo', 'fotoalu', 'alumno', 'fotoprofe', 'profesor', 'con_parte', 'comunicado',
               'cerrado']
    order_columns = ['id', 'fecha', 'grupo', '', 'alumno', '', 'profesor', 'con_parte', 'comunicado', 'cerrado']
    max_display_length = 500

    def get_initial_queryset(self):
        return self.model.objects.filter(cursoprofesor__curso=self.request.session['curso_academico_usuario'])


    def prepare_results(self, qs):
        json_data = []
        for item in qs:
            json_data.append([
                item.id,
                item.fecha.strftime("%d/%m/%Y"),
                item.get_nombre_grupo_alumno(),
                item.grupoalumno.cursoalumno.alumno.foto.url if item.grupoalumno.cursoalumno.alumno.foto else u'',
                item.get_nombre_completo_alumno(),
                item.cursoprofesor.profesor.foto.url if item.cursoprofesor.profesor.foto else u'',
                item.get_nombre_completo_profesor(),
                item.con_parte,
                item.comunicado,
                item.cerrado,
                u''
            ])
        return json_data
"""
    def render_column(self, row, column):
        if column == 'grupo':
            return row.get_nombre_grupo_alumno()
        elif column == "fotoalu":
            return row.grupoalumno.cursoalumno.alumno.url
        elif column == "alumno":
            return row.get_nombre_completo_alumno()
        elif column == "fotoprofe":
            return row.cursoprofesor.profesor.foto.url
        elif column == "profesor":
            return row.get_nombre_completo_profesor()
        else:
            return super(ParteResponsableBaseDatatableView, self).render_column(row, column)
"""