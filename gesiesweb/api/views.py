from rest_framework import viewsets
from rest_framework.routers import DefaultRouter

from alumnos.models import CursoAlumno
from grupos.models import GrupoAlumno
from .mixins import CursoAlumnoMixin, GrupoAlumnoMixin

class AlumnoViewSet(CursoAlumnoMixin, viewsets.ModelViewSet):

    def get_queryset(self):
        """
        Opcionalmente restringe los alumnos retornados a determinado curso,
        filtando contra el parametro `curso` en la URL.
        """
        queryset = CursoAlumno.objects.all().order_by('alumno__apellidos', 'alumno__nombre',)
        curso = self.request.QUERY_PARAMS.get('curso', None)
        if curso is not None:
            queryset = queryset.filter(curso__id=curso)
        return queryset


alumno_list = AlumnoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})


alumno_detail = AlumnoViewSet.as_view({
    'get': 'retrive',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


class GrupoAlumnoViewSet(GrupoAlumnoMixin, viewsets.ModelViewSet):

    def get_queryset(self):
        """
        Opcionalmente restringe los alumnos retornados a determinado curso,
        filtando contra el parametro `curso` en la URL.
        """
        queryset = GrupoAlumno.objects.all()
        cursogrupo = self.request.QUERY_PARAMS.get('cursogrupo', None)
        if cursogrupo is not None:
            queryset = queryset.filter(cursogrupo__id=cursogrupo)
        return queryset


grupoalumno_list = GrupoAlumnoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})


grupoalumno_detail = GrupoAlumnoViewSet.as_view({
    'get': 'retrive',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


router = DefaultRouter()
router.register(r'alumnos', AlumnoViewSet)
router.register(r'grupoalumnos', GrupoAlumnoViewSet)