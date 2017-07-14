from django.conf.urls import  url,include
from rest_framework import routers

#from views import ComputerViewSet
from django.contrib.auth import  views as auth_views
from .views import ComputerViewSet


urlpatterns = [
    url(r'^computer/$', ComputerViewSet.as_view({'get': 'list', 'post': 'list', 'put': 'list', 'delete': 'lis'})),
    url(r'^login/$', auth_views.login),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]
