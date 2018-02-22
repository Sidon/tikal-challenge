from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import ProcessoViewSet, TrackingViewSet


router = DefaultRouter()
router.register(r'api/processos', ProcessoViewSet, base_name='processos')
router.register(r'api/logging', TrackingViewSet)
urlpatterns = router.urls
urlpatterns += [url(r'^docs/', include('rest_framework_docs.urls'))]

