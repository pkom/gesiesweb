# -*- encoding: utf-8 -*-

from django.contrib.auth import get_user_model

from rest_framework import serializers

from cursos.models import Curso
from grupos.models import CursoGrupo, GrupoAlumno, GrupoProfesor
from partes.models import Parte

User = get_user_model()


class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = ('id', 'curso')


class CursoGrupoSerializer(serializers.ModelSerializer):

    grupo = serializers.CharField(source='grupo.grupo')
    tutor_id = serializers.IntegerField(source='tutor.id')
    tutor  = serializers.CharField(source='get_nombre_completo')
    tutor_foto = serializers.CharField(source='tutor.get_foto')

    class Meta:
        model = CursoGrupo
        fields = ( 'id', 'grupo', 'tutor_id', 'tutor', 'tutor_foto')


class CursoGruposSerializer(serializers.ModelSerializer):

    cursogrupos = CursoGrupoSerializer(many=True)

    class Meta:
        model = Curso
        fields = ('id', 'curso', 'cursogrupos')


class GrupoAlumnoSerializer(serializers.ModelSerializer):

    cursoalumno_id = serializers.IntegerField(source='cursoalumno.id')
    alumno_id = serializers.IntegerField(source='cursoalumno.alumno.id')
    alumno_nie = serializers.CharField(source='cursoalumno.alumno.nie')
    alumno = serializers.CharField(source='cursoalumno.get_nombre_completo')
    alumno_nac = serializers.DateField(source='cursoalumno.alumno.fecha_nacimiento')
    alumno_usu = serializers.CharField(source='cursoalumno.alumno.usuario_rayuela')
    alumno_foto = serializers.CharField(source='cursoalumno.get_foto')

    class Meta:
        model = GrupoAlumno
        fields = ( 'id', 'cursoalumno_id', 'alumno_id', 'alumno_nie',
                   'alumno', 'alumno_nac', 'alumno_usu', 'alumno_foto')


class CursoGrupoAlumnosDetailSerializer(serializers.ModelSerializer):

    grupo = serializers.CharField(source='grupo.grupo')
    descripcion = serializers.CharField(source='grupo.descripcion')
    tutor_id = serializers.IntegerField(source='tutor.id')
    tutor  = serializers.CharField(source='get_nombre_completo')
    tutor_foto = serializers.CharField(source='tutor.get_foto')
    grupoalumnos = GrupoAlumnoSerializer(many=True)

    class Meta:
        model = CursoGrupo
        fields = ('id', 'curso', 'grupo', 'descripcion', 'tutor_id', 'tutor', 'tutor_foto', 'grupoalumnos')


class GrupoProfesorSerializer(serializers.ModelSerializer):

    cursoprofesor_id = serializers.IntegerField(source='cursoprofesor.id')
    profesor_id = serializers.IntegerField(source='cursoprofesor.profesor.id')
    profesor_dni = serializers.CharField(source='cursoprofesor.profesor.dni')
    profesor = serializers.CharField(source='cursoprofesor.get_nombre_completo')
    profesor_usu = serializers.CharField(source='cursoprofesor.profesor.usuario_rayuela')
    profesor_foto = serializers.CharField(source='cursoprofesor.get_foto')
    es_responsable = serializers.BooleanField(source='cursoprofesor.es_responsable')

    class Meta:
        model = GrupoProfesor
        fields = ( 'id', 'cursoprofesor_id', 'profesor_id', 'profesor_dni',
                   'profesor', 'profesor_usu', 'profesor_foto', 'es_responsable')


class CursoGrupoProfesoresDetailSerializer(serializers.ModelSerializer):

    grupo = serializers.CharField(source='grupo.grupo')
    descripcion = serializers.CharField(source='grupo.descripcion')
    tutor_id = serializers.IntegerField(source='tutor.id')
    tutor  = serializers.CharField(source='get_nombre_completo')
    tutor_foto = serializers.CharField(source='tutor.get_foto')
    grupoprofesores = GrupoProfesorSerializer(many=True)

    class Meta:
        model = CursoGrupo
        fields = ('id', 'curso', 'grupo', 'descripcion', 'tutor_id', 'tutor', 'tutor_foto', 'grupoprofesores')

class ParteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parte
        fields = ('id', 'grupoalumno', 'cursoprofesor', 'fecha', 'parte', 'comunicado', 'con_parte', 'cerrado')
