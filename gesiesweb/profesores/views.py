from django.views.generic import ListView

from .models import Profesor

class ProfesorListView(ListView):
	model = Profesor