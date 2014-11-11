# -*- encoding: utf-8 -*-

from rest_framework import serializers

from alumnos.models import Alumno, CursoAlumno


class AlumnoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alumno


class CursoAlumnoSerializer(serializers.HyperlinkedModelSerializer):

    curso = serializers.Field('curso.id')
    alumno = AlumnoSerializer()

    class Meta:
        model = CursoAlumno
        fields = ('id', 'curso', 'alumno',)

