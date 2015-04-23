# -*- encoding: utf-8 -*-

from django.contrib.auth import get_user_model

from rest_framework import serializers

from cursos.models import Curso
from alumnos.models import Alumno, CursoAlumno
from profesores.models import Profesor, CursoProfesor
from partes.models import Parte, ParteSeguimiento
from grupos.models import Grupo, CursoGrupo, GrupoAlumno

User = get_user_model()

class ParteSeguimientoSerializer(serializers.ModelSerializer):

    profesor = serializers.CharField(source='get_nombre_completo', read_only=True)

    class Meta:
        model = ParteSeguimiento
        fields = ( 'id', 'parte', 'cursoprofesor', 'profesor', 'seguimiento', 'created')


class ParteSerializer(serializers.ModelSerializer):

    seguimientos = ParteSeguimientoSerializer(many=True)
    profesor = serializers.CharField(source='get_nombre_completo_profesor', read_only=True)
    alumno = serializers.CharField(source='get_nombre_completo_alumno', read_only=True)
    fotoalumno = serializers.CharField(source='get_foto_alumno_peque', read_only=True)
    fotoprofesor = serializers.CharField(source='get_foto_profesor_peque', read_only=True)


    class Meta:
        model = Parte
        fields = ( 'id', 'grupoalumno', 'fotoalumno', 'alumno', 'cursoprofesor', 'fotoprofesor', 'profesor',
                   'fecha', 'parte', 'con_parte', 'comunicado', 'cerrado', 'seguimientos')


class GrupoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grupo
        fields = ( 'id', 'grupo', 'descripcion')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ( 'id', 'username', 'first_name', 'last_name')


class ProfesorSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Profesor
        fields = ( 'id', 'user', 'dni', 'usuario_rayuela', 'foto', 'es_usuario')


class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = ( 'id', 'curso')


class CursoProfesorSerializer(serializers.ModelSerializer):

    profesor = ProfesorSerializer()
    curso = CursoSerializer()

    class Meta:
        model = CursoProfesor
        fields = ( 'id', 'curso', 'profesor', 'es_responsable')

class CursoGrupoSerializer(serializers.ModelSerializer):

    grupo = GrupoSerializer()
    tutor = CursoProfesorSerializer()
    curso = CursoSerializer()

    class Meta:
        model = CursoGrupo
        fields = ( 'id', 'curso', 'grupo', 'tutor')


class AlumnoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alumno
        fields = ( 'id', 'nie', 'apellidos', 'nombre', 'fecha_nacimiento', 'usuario_rayuela', 'foto')


class CursoAlumnoSerializer(serializers.ModelSerializer):

    alumno = AlumnoSerializer()

    class Meta:
        model = CursoAlumno
        fields = ( 'id', 'curso', 'alumno')


class GrupoAlumnoSerializer(serializers.ModelSerializer):

    cursogrupo = CursoGrupoSerializer()
    cursoalumno = CursoAlumnoSerializer()

    class Meta:
        model = GrupoAlumno
        fields = ( 'id', 'cursogrupo', 'cursoalumno')