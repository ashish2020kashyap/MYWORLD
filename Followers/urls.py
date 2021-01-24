from django.urls import path,re_path
from .views import *
from Followers import views

urlpatterns = [
    re_path(r'followers/(?P<pk>\d+)/?', follow.as_view()),
    re_path(r'allfollowers/?', all_follow.as_view()),
    re_path(r'followrud/(?P<pk>\d+)/?', followrud.as_view()),
    re_path(r'allfollowing/?', all_following.as_view()),
    re_path(r'followingrud/(?P<pk>\d+)/?', followingrud.as_view()),


    re_path(r'postfollow/(?P<pk>\d+)/?', followpost.as_view()),
    re_path(r'fetchfollow/(?P<pk>\d+)/?', following.as_view()),
    re_path(r'countfollow/(?P<pk>\d+)/?', countfollow.as_view()),


]
