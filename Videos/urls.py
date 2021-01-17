from django.contrib import admin
from django.urls import path,include,re_path
from .views import *
from Videos import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'split', SplitVideo)


urlpatterns = [
    re_path(r'trying/?', include(router.urls)),
    re_path(r'cloud/(?P<pk>\d+)/?', uploading.as_view()),
    re_path(r'upload/?', upload.as_view()),
    re_path(r'fetching/?', fetching.as_view()),
    re_path(r'chunk/?', chunkfetching.as_view()),
    re_path(r'endpointurl/?', endpoint.as_view()),
    re_path(r'single/(?P<pk>\d+)/?', singlefetching.as_view()),
    re_path(r'videolinks/(?P<pk>\d+)/?', videolinks.as_view()),
    re_path(r'allvideolinks/?', allvideolinks.as_view()),
    re_path(r'distributed/?', distributedupload.as_view()),
    re_path(r'^allvideolinks/?', allvideolinks.as_view()),
    re_path(r'somethingnew/?', something.as_view()),
]

