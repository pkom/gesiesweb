from django.contrib.auth import get_user_model

from rest_framework.generics import ListAPIView, RetrieveAPIView

from cursos.models import Curso
from grupos.models import CursoGrupo

from .serializers import CursoSerializer
from .serializers import CursoGruposSerializer, CursoGrupoAlumnosDetailSerializer, CursoGrupoProfesoresDetailSerializer
from .mixins import AuthenticateMixin


User = get_user_model()


class CursoMixin(object):

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CursoList(AuthenticateMixin, CursoMixin, ListAPIView):
    """
    Return a list of all the courses
    """
    pass

class CursoDetail(AuthenticateMixin, CursoMixin, RetrieveAPIView):
    """
    Return a specific course
    """
    pass


class GrupoList(AuthenticateMixin, RetrieveAPIView):
    """
    Return a groups by course
    """
    queryset = Curso.objects.all()
    serializer_class = CursoGruposSerializer


class GrupoAlumnosDetail(AuthenticateMixin, RetrieveAPIView):
    """
    Return a group info with students
    """
    queryset = CursoGrupo.objects.all()
    serializer_class = CursoGrupoAlumnosDetailSerializer


class GrupoProfesoresDetail(AuthenticateMixin, RetrieveAPIView):
    """
    Return a group info with teachers
    """
    queryset = CursoGrupo.objects.all()
    serializer_class = CursoGrupoProfesoresDetailSerializer