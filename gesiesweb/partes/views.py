from django.views.generic import ListView, DetailView

from .models import Parte, ParteSeguimiento

class PartesListView(ListView):

    template_name = "partes/partes.html"
    model = Parte
    context_object_name = 'partes'


class PartesDetailView(DetailView):

    template_name = "partes/detalle.html"
    model = Parte
    context_object_name = 'parte'
