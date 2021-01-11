from django.urls import path,re_path
from graphene_django.views import GraphQLView
from Profile.schema import schema
from .views import *
from Profile import views

urlpatterns = [
    # Only a single URL to access GraphQL
    re_path(r'profilegraphql/?', GraphQLView.as_view(graphiql=True, schema=schema)),
    re_path(r'allprofile/?',profile.as_view()),
    re_path(r'profilerud/(?P<pk>\d+)/?', views.profilerud.as_view()),
]
