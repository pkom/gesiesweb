from rest_framework.permissions import IsAdminUser

from alumnos.models import CursoAlumno
from grupos.models import GrupoAlumno
from .serializers import CursoAlumnoSerializer, GrupoAlumnoSerializer

class CursoAlumnoMixin(object):

    queryset = CursoAlumno.objects.all().order_by('alumno__apellidos', 'alumno__nombre',)
    serializer_class = CursoAlumnoSerializer
    permission_classes = (IsAdminUser,)


class GrupoAlumnoMixin(object):

    queryset = GrupoAlumno.objects.all()
    serializer_class = GrupoAlumnoSerializer
    permission_classes = (IsAdminUser,)
