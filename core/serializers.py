from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Processo, Logdb
from rest_framework_tracking.models import APIRequestLog


class ProcessoSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()

    class Meta:
        model = Processo
        fields = ('user','numero_processo', 'dados_processo','links')

    def get_links(self, obj):
        request = self.context['request']
        links = {'self': reverse('processo-detail', kwargs={'pk': obj.pk}, request=request)}

        if bool(request.POST):
            pass
        return links


class LogdbSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()

    class Meta:
        model = Logdb
        fields = ('post_req','post_curl','links')

    def get_links(self, obj):
        request = self.context['request']
        links = {'self': reverse('logdb-detail', kwargs={'pk': obj.pk}, request=request)}

        if bool(request.POST):
            pass
        return links


class TrackSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()

    class Meta:
        model = APIRequestLog
        fields = ('user', 'requested_at', 'path', 'remote_addr', 'host', 'method', 'query_params',
                  'data', 'response', 'status_code', 'links',
                 )

        read_only_fields = fields

    def get_links(self, obj):
        request = self.context['request']
        links = {'self': reverse('apirequestlog-detail', kwargs={'pk': obj.pk}, request=request)}

        if bool(request.POST):
            pass
        return links