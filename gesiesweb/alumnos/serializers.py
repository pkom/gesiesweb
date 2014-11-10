from rest_framework import serializers

from .models import Alumno

class AlumnoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alumno
        fields = ('nie', 'nombre', 'apellidos', 'fecha_nacimiento', 'usuario_rayuela', 'foto')
