from django.views.generic import ListView

from rest_framework import viewsets

from .models import Alumno
from .serializers import AlumnoSerializer

# Create your views here.
class ConfigListView(ListView):
    model = Alumno
    context_object_name = 'alumnos'
    template_name = 'alumnos/alumnos.html'


class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
