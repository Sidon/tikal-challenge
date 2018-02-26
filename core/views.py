from django.shortcuts import render
from django.core.exceptions import ValidationError
from rest_framework import authentication, permissions, viewsets, filters
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework_tracking.models import APIRequestLog
from .models import Processo
from .serializers import ProcessoSerializer, TrackSerializer


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

    # authentication_classes = ()
    # permission_classes = ()

    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )


class ProcessoViewSet(DefaultsMixin, LoggingMixin, viewsets.ModelViewSet):
    serializer_class = ProcessoSerializer
    search_fields = ('numero_processo' )
    queryset = Processo.objects.all()


    def get_queryset(self):
        queryset = Processo.objects.all()
        num_processo = self.request.query_params.get('numero_processo', None)
        limit = self.request.query_params.get('limit', None)
        last = self.request.query_params.get('last', None)
        empty = self.request.query_params.get('empty', None)

        if empty is not None:
            try:
                Processo.objects.all().delete()
                raise ValidationError('Empty Ok')
            except Exception as e:
                print(e)

        if num_processo is not None:
            return queryset.filter(numero_processo=num_processo)
        elif limit is not None:
            return queryset[:int(limit)]
        elif last is not None:
            return queryset.order_by('-numero_processo')[:int(last)]

        return queryset

    def perform_create(self, serializer):
        if bool(self.request.POST):
            if bool(self.request.POST):
                serializer.save ()


class TrackingViewSet(DefaultsMixin, LoggingMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = TrackSerializer
    search_fields = ('user','host', )
    queryset = APIRequestLog.objects.all()


    def get_queryset(self):
        queryset = APIRequestLog.objects.all()
        limit = self.request.query_params.get('limit', None)
        last = self.request.query_params.get('last', None)

        if limit is not None:
            queryset = queryset[:int(limit)]
        elif last is not None:
            return queryset.order_by('-numero_processo')[:int(last)]
        return queryset

def index(request):
    data = Processo.objects.all()
    print (data)
    return render(request, 'core/index.html', {'data': data} )