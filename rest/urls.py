
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls import url

urlpatterns = [
    url(r'^restapi/', include('restapi.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls'))
]

