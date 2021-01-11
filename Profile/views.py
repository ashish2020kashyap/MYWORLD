from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import ProfileSerializer
from .models import *
from django.http import HttpResponse
from time import sleep
from celery import shared_task
from asgiref.sync import sync_to_async
import time, asyncio
from authentication.models import Profile



class profile(APIView):
    def get(self, request):
        print(request.data)
        all_profile = Profile.objects.all()
        serializer = ProfileSerializer(all_profile, many=True)
        return Response(serializer.data)



class profilerud(APIView):

    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pro = self.get_object(pk)
        serializer = ProfileSerializer(pro)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        single_profile = self.get_object(pk)
        serializer = ProfileSerializer(single_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk, format=None):
        single_profile_delete = self.get_object(pk)
        single_profile_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

