from rest_framework.routers import DefaultRouter
from . import views
from django.conf.urls import url

router = DefaultRouter()
router.register(r'api/processos', views.ProcessoViewSet)
router.register(r'api/logging', views.TrackingViewSet)

urlpatterns = [
    url(r'^',views.index)

]