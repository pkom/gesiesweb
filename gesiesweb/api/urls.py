from django.conf.urls import patterns, url

from .views import CursoList, CursoDetail, GrupoList, GrupoAlumnosDetail, GrupoProfesoresDetail


urlpatterns = patterns('',

    url( r'^cursos/$', CursoList.as_view(), name='curso_list'),
    url( r'^cursodetalle/(?P<pk>[0-9]+)$', CursoDetail.as_view(), name='curso_detail'),
    url( r'^grupos/(?P<pk>[0-9]+)$', GrupoList.as_view(), name='grupo_list'),
    url( r'^grupoalumnos/(?P<pk>[0-9]+)$', GrupoAlumnosDetail.as_view(), name='grupo_alumnos_detail'),
    url( r'^grupoprofesores/(?P<pk>[0-9]+)$', GrupoProfesoresDetail.as_view(), name='grupo_profesores_detail')
)

