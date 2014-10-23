#encoding:utf-8

from django import forms
from django.contrib.auth.forms import AuthenticationForm

from cursos.models import Curso
from config.models import Config

class CourseAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'id_username',
                                                             'placeholder': 'Nombre de Usuario',
                                                             'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'id_password',
                                                             'placeholder': 'Contraseña',
                                                             'class': 'form-control'}))
    course = forms.ModelChoiceField(queryset=Curso.objects.all(),
                                    empty_label='Selecciona curso',
                                    widget=forms.Select(attrs={'id': 'id_course',
                                                               'class': 'form-control'}))

    def __init__(self, request=None, *args, **kwargs):
        super(CourseAuthenticationForm, self).__init__(request, *args, **kwargs)
        self.fields['course'].initial = Config.objects.all().first().curso_academico_defecto.id