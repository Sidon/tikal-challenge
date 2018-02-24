from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/processos', views.ProcessoViewSet)
router.register(r'api/logging', views.TrackingViewSet)
