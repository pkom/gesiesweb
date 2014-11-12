# -*- encoding: utf-8 -*-

from rest_framework import serializers

from config.models import Config
from cursos.models import Curso
from alumnos.models import Alumno, CursoAlumno
from profesores.models import Profesor


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