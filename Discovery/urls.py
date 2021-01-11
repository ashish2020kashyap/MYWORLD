from django.conf.urls import include, url
from .views import *
#from Discovery.views import *

urlpatterns = [
    url(r'^upload/$', ImageCreateAPIView.as_view()),
]