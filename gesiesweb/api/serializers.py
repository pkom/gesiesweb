# -*- encoding: utf-8 -*-

from rest_framework import serializers

from config.models import Config
from cursos.models import Curso
from alumnos.models import Alumno, CursoAlumno
from profesores.models import Profesor
from partes.models import Parte, ParteSeguimiento


class ProfesorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Profesor


class ConfigSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Config


class CursoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Curso


class AlumnoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Alumno


class CursoAlumnoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CursoAlumno


class ParteSeguimientoSerializer(serializers.ModelSerializer):

    profesor = serializers.CharField(source='get_nombre_completo', read_only=True)

    class Meta:
        model = ParteSeguimiento
        fields = ( 'id', 'parte', 'cursoprofesor', 'profesor', 'seguimiento', 'created', 'modified')


class ParteSerializer(serializers.ModelSerializer):

    seguimientos = ParteSeguimientoSerializer(many=True)
    profesor = serializers.CharField(source='get_nombre_completo_profesor', read_only=True)
    alumno = serializers.CharField(source='get_nombre_completo_alumno', read_only=True)

    class Meta:
        model = Parte
        fields = ( 'id', 'grupoalumno', 'alumno', 'cursoprofesor', 'profesor', 'fecha', 'parte', 'con_parte',
                'comunicado', 'cerrado', 'seguimientos')



