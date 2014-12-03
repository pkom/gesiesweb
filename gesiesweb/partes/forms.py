

from django.forms import models, Textarea, DateInput, CheckboxInput

from .models import Parte


class ParteForm(models.ModelForm):

    class Meta:
        model = Parte
        exclude = ('grupoalumno', 'cursoprofesor')
        widgets = {
            'fecha': DateInput(attrs={'class': 'datepicker col-xs-12', 'id':'form-field-4'}),
            'parte': Textarea(attrs={'class': 'col-xs-12', 'rows': 10, 'id':'form-field-5'}),
            'con_parte': CheckboxInput(attrs={'class': 'col-xs-12 col-sm-5', 'id':'form-field-6'}),
            'comunicado': CheckboxInput(attrs={'class': 'col-xs-12 col-sm-5', 'id':'form-field-7'}),
            'cerrado': CheckboxInput(attrs={'class': 'col-xs-12 col-sm-5', 'id':'form-field-8'}),
        }
