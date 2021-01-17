from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import *

from rest_framework import status
from rest_framework.response import Response


class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = ['id','user','title','category','upload_file','timestamp']


class ChunkUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChunkUpload
        fields = ['id','video_id','video_length','thumbnail','chunk1','chunk2','chunk3','chunk4']


class ChunkFetchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChunkUpload
        fields = ['id','video_id','video_length','thumbnail','chunk1','chunk2','chunk3','chunk4','view_count']



class fetchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = ['upload_file']

