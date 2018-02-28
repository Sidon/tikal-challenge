import django_tables2 as tables
from django_tables2.utils import A
from .models import Processo


class ProcessoTable(tables.Table):

    # account_number = tables.LinkColumn('customer-detail', args=[A('pk')])

    class Meta:
        template_name = 'django_tables2/bootstrap-responsive.html'
        model = Processo
        fields = ('user','numero_processo','dados_processo')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "Não encontrado!"