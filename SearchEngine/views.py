from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import SearchSerializer
from .models import *
from django.http import HttpResponse
from django.http import Http404
from rest_framework import generics
from authentication.models import User
from rest_framework import filters

'''
class Searching(generics.ListAPIView):
    serializer_class = SearchSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        return User.objects.filter(username=username)
    
'''

'''
class DynamicSearching(generics.ListCreateAPIView):
    search_fields = ['username']
    filter_backends = (filters.SearchFilter,)
    queryset = User.objects.all()
    serializer_class = SearchSerializer

'''
class DynamicSearching(generics.ListAPIView):
    search_fields = ['username']
    filter_backends = (filters.SearchFilter,)
    queryset = User.objects.all()
    serializer_class = SearchSerializer
