from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView
from django.core.urlresolvers import reverse

from .models import Usuario

# Create your views here.
class UsuarioListView(ListView):
	model = Usuario