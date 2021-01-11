from django.urls import path,re_path
from graphene_django.views import GraphQLView
from GraphQl.schema import schema

urlpatterns = [
    # Only a single URL to access GraphQL
    re_path(r'graphql/?', GraphQLView.as_view(graphiql=True, schema=schema)),
]
