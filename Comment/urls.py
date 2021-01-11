from django.urls import path,re_path
from .views import *
from Comment import views

urlpatterns = [
    re_path(r'allcomments/?', all_comment.as_view()),

]