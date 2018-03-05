from collections import namedtuple
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView
from django_tables2 import RequestConfig
from django.core.exceptions import ValidationError
from rest_framework import authentication, permissions, viewsets, filters
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework_tracking.models import APIRequestLog
from .models import Processo, Logdb
from .serializers import ProcessoSerializer, TrackSerializer, LogdbSerializer
from .tables import ProcessoTable, LogdbTable
from .forms import ProcessoForm
from util.logapi import Log_api

log_api = Log_api()

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


    def _perform(self, anterior):
        self.request.query_params._mutable = True
        self.request.query_params['user'] = self.request.user

        return  {"user_id": str(self.request.user), "numero_processo": self.request.POST.get("numero_processo"),
                "dados_atual": self.request.POST.get("dados_processo"),
                "dados_anterior": anterior}


    def perform_create(self, serializer):
        data = self._perform('')
        log_api.update_api(data)
        serializer.save()


    def perform_update(self, serializer):
        anterior = Processo.objects.filter(numero_processo=self.request.POST.get('numero_processo'))[0].dados_processo
        data = self._perform(anterior)
        log_api.update_api(data)
        serializer.save()


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


class LogPostsViewSet(DefaultsMixin, LoggingMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = LogdbSerializer
    queryset =Logdb.objects.all()

    def get_queryset(self):
        queryset = Logdb.objects.all()
        limit = self.request.query_params.get('limit', None)
        last = self.request.query_params.get('last', None)

        if limit is not None:
            queryset = queryset[:int(limit)]
        elif last is not None:
            return queryset[:int(last)]
        return queryset


class ProcessoListView(ListView):
    model = Processo
    template_name = 'core/processo_list.html'
    context_object_name = 'processo'

    def get_context_data(self, **kwargs):
        context = super(ProcessoListView, self).get_context_data(**kwargs)
        table = ProcessoTable(Processo.objects.all().order_by('-pk'))
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context



class LogdbListView(ListView):
    model = Logdb
    template_name = 'core/log_posts_list.html'
    context_object_name = 'logdb'

    def get_context_data(self, **kwargs):
        context = super(LogdbListView, self).get_context_data(**kwargs)
        table = LogdbTable(Logdb.objects.all().order_by('-pk'))
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context


def _log_post(obj, before, rq):

    data = {"user_id": str(rq.user), "numero_processo": obj.numero_processo,
            "dados_atual": obj.dados_processo, "dados_anterior": before}
    log_api.update_api(data)


class ProcessoCreateView(CreateView):
    model = Processo
    template_name = 'core/processo-create.html'
    form_class = ProcessoForm
    success_url = '/processos'

    def form_valid(self, form):
        structs = namedtuple('structs', 'dados_processo numero_processo id')
        d1 = form.cleaned_data
        obj = structs(dados_processo=d1['dados_processo'], numero_processo=d1['numero_processo'], id=str(d1['user']))

        _log_post(obj, "", self.request)
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())


class ProcessoUpdateView(UpdateView):
    model = Processo
    template_name = 'core/processo-create.html'
    form_class = ProcessoForm
    success_url = '/processos'

    def form_valid(self, form,):
        before = Processo.objects.filter(pk=self.object.id)[0]
        if not (before.dados_processo == self.object.dados_processo):

            print ('Objjjjject-->',self.object)
            _log_post(self.object, before.dados_processo, self.request)


        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

