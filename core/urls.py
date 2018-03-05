from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'core'

router = DefaultRouter()
router.register(r'api/processos', views.ProcessoViewSet)
router.register(r'api/log-posts', views.LogPostsViewSet)
router.register(r'api/logging', views.TrackingViewSet)


urlpatterns = [
    url(r'^$', views.ProcessoListView.as_view(), name='home'),
    url(r'processos/', views.ProcessoListView.as_view(), name='processos'),
    url(r'log-posts/', views.LogdbListView.as_view(), name='logposts'),
    url('^update-processo/(?P<pk>[\w-]+)$', views.ProcessoUpdateView.as_view(), name='update1'),
    url(r'cadastro/', views.ProcessoCreateView.as_view(), name='cadastro'),
]


