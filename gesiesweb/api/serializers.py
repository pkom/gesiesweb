# -*- encoding: utf-8 -*-

from rest_framework import serializers

from alumnos.models import CursoAlumno
from grupos.models import GrupoAlumno


class CursoAlumnoSerializer(serializers.ModelSerializer):

    alumno = serializers.Field(source=u'alumno.apellidos')

    class Meta:
        model = CursoAlumno
        fields = ('id', 'curso', 'alumno',)

class GrupoAlumnoSerializer(serializers.ModelSerializer):

    class Meta:
        model = GrupoAlumno
        fields = ('id', 'cursogrupo', 'cursoalumno',)