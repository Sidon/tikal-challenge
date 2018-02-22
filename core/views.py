from django.core.exceptions import ValidationError

# DRF
from rest_framework import viewsets
from rest_framework import authentication, permissions, viewsets, filters, pagination
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework_tracking.models import APIRequestLog

from .models import Processo
from .serializers import ProcessoSerializer, TrackSerializer
from .forms import ProcessoFilter

class DefaultsMixin(object):
    """Default settings for view authentication, permissions, filtering
     and pagination."""

    authentication_classes = (
         authentication.BasicAuthentication,
         authentication.TokenAuthentication,
    )
    permission_classes = (
         permissions.IsAuthenticated,
    )

    # pagination_class = pagination.PageNumberPagination
    # paginate_by = 10

    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )


class ProcessoViewSet(DefaultsMixin, viewsets.ModelViewSet):
    '''
     
    API endpoint that allows processos to view
    
    retrieve:    
    Return a processo instance.
        
    list:    
    Return a list of all processo. For view a instance,
    click in *instance* link
    
    '''
    queryset = Processo.objects.all()
    serializer_class = ProcessoSerializer
    search_fields = ('numero_processo', )
    # lookup_field = 'name'
    http_method_names = ['get', 'head']
    filter_class = ProcessoFilter


class TrackingViewSet(DefaultsMixin, LoggingMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = TrackSerializer
    search_fields = ('user','host', )
    queryset = APIRequestLog.objects.all()


    def get_queryset(self):
        queryset = APIRequestLog.objects.all()
        limit = self.request.query_params.get('limit', None)

        if limit is not None:
            queryset = queryset[:int(limit)]
        return queryset
