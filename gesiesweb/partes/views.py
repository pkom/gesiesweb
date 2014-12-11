# -*- coding: utf-8 -*-
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView
from sorl.thumbnail import get_thumbnail
from django_datatables_view.base_datatable_view import BaseDatatableView

from core.mixins import LoginRequerido, ResponsableRequiredMixin

from grupos.models import GrupoAlumno
from .models import Parte, ParteSeguimiento
from .forms import ParteForm


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
    fields = ['fecha', 'parte', 'comunicado']

    def get_initial(self):
        return { 'fecha' : timezone.now() }

    def form_valid(self, form):

        grupoalumno = GrupoAlumno.objects.get(pk=124)
        form.instance.grupoalumno = grupoalumno
        form.instance.cursoprofesor = self.request.session['curso_profesor']
        return super(ParteCreateView, self).form_valid(form)


class ParteDetailView(LoginRequerido, DetailView):

    template_name = "partes/detalle.html"
    model = Parte
    context_object_name = 'parte'


class ParteUpdateView(LoginRequerido, UpdateView):

    template_name = "partes/editar.html"
    model = Parte
    form_class = ParteForm
    success_url = reverse_lazy("parte:partes-responsable")

    def form_valid(self, form):
        print "Formulario VALIDO"
        print form.instance
        form.instance.cursoprofesor = self.request.session['curso_profesor']
        return super(ParteUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        print "Formulario NO VALIDO"
        print form
        return super(ParteUpdateView, self).form_invalid(form)


class ParteDeleteView(ResponsableRequiredMixin, DeleteView):

    model = Parte
    template_name = "partes/borrar.html"
    success_url = reverse_lazy("parte:partes-responsable")


class ParteResponsableTemplateView(ResponsableRequiredMixin, TemplateView):

    template_name = "partes/partes_responsablesjq.html"

    def get_context_data(self, **kwargs):
        context = super(ParteResponsableTemplateView, self).get_context_data(**kwargs)
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


class ParteResponsableListView(ResponsableRequiredMixin, TemplateView):

    template_name = "partes/partes_responsables.html"

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


class ParteResponsableBaseDatatableView(ResponsableRequiredMixin, BaseDatatableView):

    model = Parte
    columns = ['id', 'fecha', 'grupo', 'fotoalu', 'alumno', 'fotoprofe', 'profesor', 'con_parte', 'comunicado',
               'cerrado', 'parte', 'urls']
    order_columns = ['id', 'fecha', 'grupoalumno__cursogrupo__grupo__grupo', '',
                     ['grupoalumno__cursoalumno__alumno__apellidos','grupoalumno__cursoalumno__alumno__nombre' ], '',
                     ['cursoprofesor__profesor__user__last_name', 'cursoprofesor__profesor__user__first_name' ],
                     'con_parte', 'comunicado', 'cerrado', '', '']
    max_display_length = 500


    def get_initial_queryset(self):

        return self.model.objects.filter(cursoprofesor__curso=self.request.session['curso_academico_usuario'])


    def filter_queryset(self, qs):

        search = self.request.GET.get('search[value]', None)
        if search:
            cadena = search.split('/')
            haydia = False
            haymes = False
            hayanio = False
            try:
                dia = int(cadena[0])
            except:
                pass
            else:
                haydia = True
            try:
                mes = int(cadena[1])
            except:
                pass
            else:
                haymes = True
            try:
                anio = int(cadena[2])
            except:
                pass
            else:
                hayanio = True
            q = Q(grupoalumno__cursogrupo__grupo__grupo__icontains=search)
            q = q | Q(grupoalumno__cursoalumno__alumno__apellidos__icontains=search)
            q = q | Q(grupoalumno__cursoalumno__alumno__nombre__icontains=search)
            q = q | Q(cursoprofesor__profesor__user__last_name__icontains=search)
            q = q | Q(cursoprofesor__profesor__user__first_name__icontains=search)
            if haydia:
                q = q | Q(fecha__day=dia)
            if haymes:
                q = q & Q(fecha__month=mes)
            if hayanio:
                q = q & Q(fecha__year=anio)
            qs = qs.filter(q)
        return qs


    def prepare_results(self, qs):
        data = []
        for item in qs:
            row = {'DT_RowId': item.id}
            for column in self.get_columns():
                row[column] = self.render_column(item, column)
            data.append(row)
#                [self.render_column(item, column) for column in self.get_columns()])
        return data


    def render_column(self, row, column):

        if column == "id":
            return {'id': row.id,
                    'display': reverse_lazy('parte:detalle', args=[row.id])
            }
        elif column == "fecha":
            return  row.fecha.strftime("%d/%m/%Y")
        elif column == 'grupo':
            return row.get_nombre_grupo_alumno()
        elif column == "fotoalu":
            if row.grupoalumno.cursoalumno.alumno.foto:
                return get_thumbnail(row.grupoalumno.cursoalumno.alumno.foto, '50x40').url
            else:
                return u''
        elif column == "alumno":
            return row.get_nombre_completo_alumno()
        elif column == "fotoprofe":
            if row.cursoprofesor.profesor.foto:
                return get_thumbnail(row.cursoprofesor.profesor.foto, '50x40').url
            else:
                return u''
        elif column == "profesor":
            return row.get_nombre_completo_profesor()
        elif column == "urls":
            return {
                'detalle': reverse_lazy('parte:detalle', args=[row.id]),
                'editar': reverse_lazy('parte:editar', args=[row.id]),
                'eliminar': reverse_lazy('parte:eliminar', args=[row.id])
            }
        else:
            return super(ParteResponsableBaseDatatableView, self).render_column(row, column)
