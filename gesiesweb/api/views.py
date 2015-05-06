from rest_framework import viewsets

from grupos.models import CursoGrupo, GrupoAlumno
from partes.models import Parte, ParteSeguimiento

from .serializers import ParteSerializer, ParteSeguimientoSerializer, CursoGrupoSerializer, GrupoAlumnoSerializer
from .mixins import AuthenticateMixin


class CursoGrupoViewSet(AuthenticateMixin, viewsets.ModelViewSet):

    model = CursoGrupo
    serializer_class = CursoGrupoSerializer
    filter_fields = ('id', 'curso__id', 'grupo__id', 'tutor__id')

class GrupoAlumnoViewSet(AuthenticateMixin, viewsets.ModelViewSet):

    model = GrupoAlumno
    serializer_class = GrupoAlumnoSerializer


class ParteViewSet(AuthenticateMixin, viewsets.ModelViewSet):

#    model = Parte
    queryset = Parte.objects.all()
    serializer_class = ParteSerializer


class ParteSeguimientoViewSet(AuthenticateMixin, viewsets.ModelViewSet):

    model = ParteSeguimiento
    serializer_class = ParteSeguimientoSerializer

