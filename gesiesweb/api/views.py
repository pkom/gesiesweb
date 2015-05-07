from django.contrib.auth import get_user_model

from rest_framework import viewsets, mixins

from cursos.models import Curso
from grupos.models import CursoGrupo, GrupoAlumno
from partes.models import Parte, ParteSeguimiento

from .serializers import CursoSerializer
from .serializers import ParteSerializer, ParteSeguimientoSerializer, CursoGrupoSerializer, GrupoAlumnoSerializer
from .mixins import AuthenticateMixin


User = get_user_model()


class CursoMixin(object):

    queryset = Curso.objects.all()


class CursoViewSet(AuthenticateMixin, CursoMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):

    serializer_class = CursoSerializer


class CursoGrupoViewSet(AuthenticateMixin, CursoMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):

    serializer_class = CursoGrupoSerializer


class GrupoAlumnoViewSet(AuthenticateMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):

    model = GrupoAlumno
    serializer_class = GrupoAlumnoSerializer


class ParteViewSet(AuthenticateMixin, viewsets.ModelViewSet):

#    model = Parte
    queryset = Parte.objects.all()
    serializer_class = ParteSerializer


class ParteSeguimientoViewSet(AuthenticateMixin, viewsets.ModelViewSet):

    model = ParteSeguimiento
    serializer_class = ParteSeguimientoSerializer

