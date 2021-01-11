from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import UploadSerializer, fetchSerializer,ChunkUploadSerializer
from .models import *
from .tasks import sleepy, videoupload,preprocess
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import json
from django.http import HttpResponse
# import serializer from rest_framework
from rest_framework import serializers

import os
import os.path
import subprocess


class uploading(APIView):

    def get(self, request, pk):
        video_1 = Upload.objects.all()
        video_2 = video_1.filter(user=pk)
        serializer = UploadSerializer(video_2, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class upload(APIView):
    def post(self, request):
        serializer = UploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class fetching(APIView):

    def get(self, request):
        video_1 = Upload.objects.all()
        serializer = UploadSerializer(video_1, many=True)
        return Response(serializer.data)


class singlefetching(APIView):

    def get(self, request, pk):
        video_1 = Upload.objects.all()
        video_2 = video_1.filter(user=pk)
        serializer = UploadSerializer(video_2, many=True)
        return Response(serializer.data)


class videolinks(APIView):

    def get(self, request, pk):
        video_1 = Upload.objects.all().filter(user=pk)
        serializer = fetchSerializer(video_1, many=True)
        return Response(serializer.data)


class allvideolinks(APIView):

    def get(self, request):
        video_1 = Upload.objects.all()
        serializer = fetchSerializer(video_1, many=True)
        return Response(serializer.data)

'''
class distributedupload(APIView):
    def post(self, request):
        # videoupload.delay()
        # sleepy.delay(30)
        serializer = UploadSerializer(data=request.data)
        user = request.data.get('user')
        title = request.data.get('title')
        # file = request.data.get('upload_file')
        # file=request.FILES['upload_file'].temporary_file_path()
        # print(file)
        # file = request.FILES['upload_file']
        # file_name = f'avatar-{request.user.id}.jpg'
        # file_path = f'{settings.BASE_DIR}/static/{file_name}'
        # file = request.data['upload_file']
        # print(file)
        # videoupload.delay(user, title, file)
        return Response("completed")

'''

class distributedupload(APIView):
    def post(self, request):
        user = request.data.get('user')
        title = request.data.get('title')
        myfile=request.FILES['upload_file']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        uploaded_file_url=fs.url(filename)
        #print(uploaded_file_url)
        print(filename)
        urlss="http://"+settings.AWS_S3_CUSTOM_DOMAIN+uploaded_file_url

        try:
            #data=videoupload.delay(user, title, urlss)
            data = videoupload.delay(user, title, filename)
            print(data.task_id)
            print("http://"+settings.AWS_S3_CUSTOM_DOMAIN+uploaded_file_url)

        except:
            print("some error")

        return Response("completed")




class something(APIView):
    def post(self, request):
        serializer = UploadSerializer(data=request.data)
        if serializer.is_valid():
            print("inside saving serializer")
            obj=serializer.save()
            print("serializer saved")
            video_id=obj.id
            data = preprocess.delay(video_id)
            print(video_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class chunkfetching(APIView):

    def get(self, request):
        video_1 = ChunkUpload.objects.all()
        serializer = ChunkUploadSerializer(video_1, many=True)
        return Response(serializer.data)


class endpoint(APIView):
    def post(self, request):
        serializer = ChunkUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)