from rest_framework import viewsets
from rest_framework.routers import DefaultRouter
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from alumnos.models import CursoAlumno
from api.serializers import CursoAlumnoSerializer

class CursoAlumnoMixin(object):
    queryset = CursoAlumno.objects.all().order_by('alumno__apellidos', 'alumno__nombre',)
    serializer_class = CursoAlumnoSerializer
    permission_classes = (IsAdminUser,)


class AlumnoViewSet(CursoAlumnoMixin, viewsets.ModelViewSet):
    pass

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

alumno_router = DefaultRouter()
alumno_router.register(r'alumnos', AlumnoViewSet)