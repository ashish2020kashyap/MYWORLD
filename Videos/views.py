from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import UploadSerializer, fetchSerializer,ChunkUploadSerializer,ChunkFetchSerializer,IpsSerializer
from .models import *
from rest_framework import routers, serializers, viewsets
from .tasks import sleepy, videoupload,preprocess
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import json
from django.http import HttpResponse
# import serializer from rest_framework
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
import os
import os.path
import subprocess
from authentication.models import User
from django.db.models import Q


class uploading(APIView):
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = UploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class fetching(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        video_1 = Upload.objects.all()
        serializer = UploadSerializer(video_1, many=True)
        return Response(serializer.data)


class singlefetching(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        video_1 = Upload.objects.all()
        video_2 = video_1.filter(user=pk)
        serializer = UploadSerializer(video_2, many=True)
        return Response(serializer.data)


class videolinks(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        video_1 = Upload.objects.all().filter(user=pk)
        serializer = fetchSerializer(video_1, many=True)
        return Response(serializer.data)


class allvideolinks(APIView):
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]

    def get(self, request):
        video_1 = ChunkUpload.objects.all()
        serializer = ChunkUploadSerializer(video_1, many=True)
        return Response(serializer.data)



class SplitVideo(viewsets.ModelViewSet):
    serializer_class = ChunkFetchSerializer
    queryset=ChunkUpload.objects.order_by('view_count')

    def retrieve(self, request,pk, *args, **kwargs):
        print(pk)
        obj = self.get_object()
        obj.view_count = obj.view_count + 1
        obj.save(update_fields=("view_count", ))
        return super().retrieve(request, *args, **kwargs)

    def list(self, request,pk, *args, **kwargs):
        print(pk)
        # You could also increment the view count if people see the `Notice` in a listing.
        queryset = self.filter_queryset(self.get_queryset())
        for obj in queryset:
            obj.view_count = obj.view_count + 1
            obj.save(update_fields=("view_count", ))
        return super().list(request, *args, **kwargs)





class countvideo(APIView):



    def get(self, request, pk):
        def get_ip(request):
            adress = request.META.get('HTTP_X_FORWARDED_FOR')
            if adress:
                ip = adress.split(',')[-1].strip()
            else:
                ip = request.META.get('REMOTE_ADDR')

            return ip

        video_1 = ChunkUpload.objects.all()
        video_2 = video_1.filter(video_id=pk)
        serializer = ChunkFetchSerializer(video_2, many=True)
        singlevideo = ChunkUpload.objects.get(id=pk)

        ip = get_ip(request)
        u = IPS(video=singlevideo,user=ip)
        print(ip)
        #result = IPS.objects.filter(Q(user_icontains=ip))
        result = IPS.objects.filter(user=ip)
        idfinding= IPS.objects.filter(video=pk)
        print(idfinding)

        if len(result) == 1 and len(idfinding)==1:
            print("user exist")

        elif len(result) > 1 and len(idfinding)>1:
            print("user exist more")

        else:
            u.save()
            print("user is unique")
        counting = IPS.objects.all().count()
        print(counting)


        return Response(serializer.data)












class endpoint(APIView):
    def post(self, request):
        serializer = ChunkUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class viewscount(APIView):

    def get(self, request, pk):
        video_1 = IPS.objects.all()
        count = video_1.filter(video=pk).count()
        return Response(
            {
                'video_id': pk,
                'views': count
            }

        )