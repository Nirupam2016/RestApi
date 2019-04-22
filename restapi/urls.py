from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from restapi import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.StockList.as_view()),
    url(r'^(?P<pk>\d+)/$', views.StockDetails.as_view()),

]

