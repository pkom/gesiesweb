from rest_framework import viewsets
from rest_framework.routers import SimpleRouter,DefaultRouter

from config.models import Config
from cursos.models import Curso
from alumnos.models import Alumno, CursoAlumno
from asignaturas.models import Asignatura, DepartamentoAsignatura
from departamentos.models import Departamento, CursoDepartamento, DepartamentoProfesor
from grupos.models import Grupo, CursoGrupo, GrupoAlumno, GrupoProfesor
from profesores.models import Profesor, CursoProfesor

from .serializers import CursoSerializer, ConfigSerializer, ProfesorSerializer, AlumnoSerializer, CursoAlumnoSerializer
from .mixins import AuthenticateMixin


class ConfigViewSet(AuthenticateMixin, viewsets.ModelViewSet):

    model = Config
    serializer_class = ConfigSerializer


class CursoViewSet(AuthenticateMixin, viewsets.ModelViewSet):

    model = Curso
    serializer_class = CursoSerializer


class AlumnoViewSet(AuthenticateMixin, viewsets.ModelViewSet):

    model = Alumno
    serializer_class = AlumnoSerializer
    filter_fields = ('nie', 'apellidos', 'nombre',)

class CursoAlumnoViewSet(AuthenticateMixin, viewsets.ModelViewSet):

    model = CursoAlumno
    serializer_class = CursoAlumnoSerializer
    filter_fields = ('curso', 'id', 'alumno__nie', 'alumno__apellidos', 'alumno__nombre',)


class AsignaturaViewSet(AuthenticateMixin, viewsets.ModelViewSet):

    model = Asignatura


class DepartamentoViewSet(AuthenticateMixin, viewsets.ModelViewSet):

    model = Departamento


class CursoDepartamentoViewSet(AuthenticateMixin, viewsets.ModelViewSet):

    model = CursoDepartamento


class DepartamentoProfesorViewSet(AuthenticateMixin, viewsets.ModelViewSet):

    model = DepartamentoProfesor

class DepartamentoAsignaturaViewSet(AuthenticateMixin, viewsets.ModelViewSet):

    model = DepartamentoAsignatura


class GrupoViewSet(AuthenticateMixin, viewsets.ModelViewSet):

    model = Grupo


class CursoGrupoViewSet(AuthenticateMixin, viewsets.ModelViewSet):

    model = CursoGrupo


class GrupoAlumnoViewSet(AuthenticateMixin, viewsets.ModelViewSet):

    model = GrupoAlumno


class GrupoProfesorViewSet(AuthenticateMixin, viewsets.ModelViewSet):

    model = GrupoProfesor


class ProfesorViewSet(AuthenticateMixin, viewsets.ModelViewSet):

    model = Profesor


class CursoProfesorViewSet(AuthenticateMixin, viewsets.ModelViewSet):

    model = CursoProfesor
    serializer_class = ProfesorSerializer


router = DefaultRouter()
router.register(r'config', ConfigViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'alumnos', AlumnoViewSet)
router.register(r'cursoalumnos', CursoAlumnoViewSet)
router.register(r'asignaturas', AsignaturaViewSet)
router.register(r'departamentos', DepartamentoViewSet)
router.register(r'cursodepartamentos', CursoDepartamentoViewSet)
router.register(r'departamentoprofesores', DepartamentoProfesorViewSet)
router.register(r'departamentoasignaturas', DepartamentoAsignaturaViewSet)
router.register(r'grupos', GrupoViewSet)
router.register(r'cursogrupos', CursoGrupoViewSet)
router.register(r'grupoalumnos', GrupoAlumnoViewSet)
router.register(r'grupoprofesores', GrupoProfesorViewSet)
router.register(r'profesores', ProfesorViewSet)
router.register(r'cursoprofesores', CursoProfesorViewSet)





