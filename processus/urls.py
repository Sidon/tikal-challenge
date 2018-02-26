
from django.conf.urls import include, url
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from controlcenter.views import controlcenter

from core.urls import router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'admin/dashboard/', controlcenter.urls),
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/', include(router.urls)),
    url(r'', include('core.urls')),
]

