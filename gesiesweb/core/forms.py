#encoding:utf-8

from django import forms
from django.contrib.auth.forms import AuthenticationForm

from cursos.models import Curso

class CourseAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'id_username',
                                                             'placeholder': 'Nombre de Usuario',
                                                             'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'id_password',
                                                             'placeholder': 'Contraseña',
                                                             'class': 'form-control'}))
    course = forms.ModelChoiceField(queryset=Curso.objects.all(),widget=forms.Select())

