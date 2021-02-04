from django.urls import path,re_path
from .views import *
from SearchEngine import views

urlpatterns = [
    #re_path('^searching/(?P<username>.+)/$', Searching.as_view()),
    re_path(r'dynamic/?', DynamicSearching.as_view()),

]