# -*- coding: utf-8 -*-

import datetime

from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, CreateView, DetailView

from sorl.thumbnail import get_thumbnail
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
    order_columns = ['id', 'fecha', 'grupoalumno__cursogrupo__grupo__grupo', '',
                     ['grupoalumno__cursoalumno__alumno__apellidos','grupoalumno__cursoalumno__alumno__nombre' ], '',
                     ['cursoprofesor__profesor__user__last_name', 'cursoprofesor__profesor__user__first_name' ],
                     'con_parte', 'comunicado', 'cerrado']
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
            return {'_': row.id,
                    'display': u'<a href="%s">%s</a>' % (reverse_lazy('parte:detalle', args=[row.id]), row.id)
            }
        elif column == "fecha":
            return  row.fecha.strftime("%d/%m/%Y")
        elif column == 'grupo':
            return row.get_nombre_grupo_alumno()
        elif column == "fotoalu":
            if row.grupoalumno.cursoalumno.alumno.foto:
                fotoalu = get_thumbnail(row.grupoalumno.cursoalumno.alumno.foto, '50x40')
                return u'<img class="nav-user-photo" style="border-radius: 15px;" src="%s">' % (fotoalu.url,)
            else:
                return u''
        elif column == "alumno":
            return row.get_nombre_completo_alumno()
        elif column == "fotoprofe":
            if row.cursoprofesor.profesor.foto:
                fotopro = get_thumbnail(row.cursoprofesor.profesor.foto, '50x40')
                return u'<img class="nav-user-photo" style="border-radius: 15px;" src="%s">' % (fotopro.url,)
            else:
                return u''
        elif column == "profesor":
            return row.get_nombre_completo_profesor()
        elif column == "con_parte":
            if row.con_parte:
                return u'<input type="checkbox" checked="checked">'
            else:
                return u'<input type="checkbox">'
                #return u'<i class="ace-icon fa fa-check bigger-120"></i>'
        elif column == "comunicado":
            if row.comunicado:
                return u'<input type="checkbox" checked="checked">'
            else:
                return u'<input type="checkbox">'
                #return u'<i class="ace-icon fa fa-check bigger-120"></i>'
        elif column == "cerrado":
            if row.cerrado:
                return u'<input type="checkbox" checked="checked">'
            else:
                return u'<input type="checkbox">'
                #return u'<i class="ace-icon fa fa-check bigger-120"></i>'
        elif column == "acciones":
            return u"""<div class="hidden-sm hidden-xs action-buttons">
                            <a class="blue tooltip-info" href="%s" data-rel="tooltip" title="Ver parte" data-original-title="Ver">
                                <i class="ace-icon fa fa-search-plus bigger-130"></i>
                            </a>

                            <a class="green tooltip-success" href="%s" data-rel="tooltip" title="Edita parte" data-original-title="Edita">
                                <i class="ace-icon fa fa-pencil bigger-130"></i>
                            </a>

                            <a class="red tooltip-error" href="%s" data-rel="tooltip" title="Elimina parte" data-original-title="Elimina">
                                <i class="ace-icon fa fa-trash-o bigger-130"></i>
                            </a>

                        </div>
                        <div class="hidden-md hidden-lg">
                            <div class="inline position-relative">
                                <button class="btn btn-minier btn-yellow dropdown-toggle" data-toggle="dropdown" data-position="auto">
                                    <i class="ace-icon fa fa-caret-down icon-only bigger-120"></i>
                                </button>

                                <ul class="dropdown-menu dropdown-only-icon dropdown-yellow dropdown-menu-right dropdown-caret dropdown-close">
                                    <li>
                                        <a href="%s" class="tooltip-info" data-rel="tooltip" title="Ver parte" data-original-title="Ver">
                                            <span class="blue">
                                                <i class="ace-icon fa fa-search-plus bigger-120"></i>
                                            </span>
                                        </a>
                                    </li>

                                    <li>
                                        <a href="%s" class="tooltip-success" data-rel="tooltip" title="Edita parte" data-original-title="Edita">
                                            <span class="green">
                                                <i class="ace-icon fa fa-pencil-square-o bigger-120"></i>
                                            </span>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="%s" class="tooltip-error" data-rel="tooltip" title="Elimina" data-original-title="Elimina">
                                            <span class="red">
                                                <i class="ace-icon fa fa-trash-o bigger-120"></i>
                                            </span>
                                        </a>
                                    </li>
                                </ul>
                            </div>
                        </div>""" % (reverse_lazy('parte:detalle', args=[row.id]),
                                reverse_lazy('parte:editar', args=[row.id]),
                                reverse_lazy('parte:eliminar', args=[row.id]),
                                reverse_lazy('parte:detalle', args=[row.id]),
                                reverse_lazy('parte:editar', args=[row.id]),
                                reverse_lazy('parte:eliminar', args=[row.id]))
        else:
            return super(ParteResponsableBaseDatatableView, self).render_column(row, column)
