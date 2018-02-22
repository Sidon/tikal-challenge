import django_filters
from .models import Processo


class ProcessoFilter(django_filters.FilterSet):

    class Meta:
        model = Processo
        fields = ('numero_processo',)


