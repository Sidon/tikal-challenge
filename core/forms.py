from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from material import *
import django_filters
from .models import Processo

class ProcessoFilter(django_filters.FilterSet):

    class Meta:
        model = Processo
        fields = ('numero_processo',)



class ProcessoForm(ModelForm):
    class Meta:
        model = Processo

        fields = ['user', 'numero_processo', 'dados_processo']


class ProcessoForm_material(forms.Form):

        user = forms.ModelChoiceField(queryset=User.objects.all())
        num  = forms.CharField()
        dados = forms.Textarea()


        layout = Layout(
            Fieldset('Dados do processo',
                     Row(Span5('user'), Span5('num')),
                     Row('dados'))
        )
