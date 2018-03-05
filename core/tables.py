from django.urls import reverse
import django_tables2 as tables
from django_tables2.utils import A
from .models import Processo, Logdb

class ProcessoTable(tables.Table):
    numero_processo = tables.LinkColumn(args=[A('pk')], attrs={'class': 'edit'}, viewname='core:update1')
    class Meta:
        template_name = 'django_tables2/bootstrap-responsive.html'
        model = Processo
        fields = ('numero_processo','user','dados_processo')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "Não encontrado!"

class LogdbTable(tables.Table):
    class Meta:
        template_name = 'django_tables2/bootstrap-responsive.html'
        model = Logdb
        fields = ('id','post_req','post_curl')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "Não encontrado!"
