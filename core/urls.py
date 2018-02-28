from django.conf.urls import url
from django.views.generic import list, detail
from rest_framework.routers import DefaultRouter
from . import views
from .models import Processo

app_name = 'core'


router = DefaultRouter()
router.register(r'api/processos', views.ProcessoViewSet)
router.register(r'api/logging', views.TrackingViewSet)

urlpatterns = [
    # url(r'^$',views.index),
    url(r'processos/', views.ProcessoListView.as_view(), name='processos'),
    url(r'cadastro/', views.ProcessoCreateView.as_view(), name='cadastro'),
]