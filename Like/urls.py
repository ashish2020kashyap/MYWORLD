from django.urls import path,re_path
from .views import *
from Like import views

urlpatterns = [
    re_path(r'alllikes/?',all_like.as_view()),

]