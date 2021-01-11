from django.urls import path,re_path
from .views import *
from Followers import views

urlpatterns = [
    re_path(r'followers/<int:pk>/?', follow.as_view()),
    re_path(r'allfollowers/?', all_follow.as_view()),
    re_path(r'followrud/<int:pk>/?', followrud.as_view()),
    re_path(r'followings/<int:pk>/?', following.as_view()),
    re_path(r'allfollowing/?', all_following.as_view()),
    re_path(r'followingrud/<int:pk>/?', followingrud.as_view()),

]
