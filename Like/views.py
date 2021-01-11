from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import LikeSerializer
from .models import *
from django.http import HttpResponse


class all_like(APIView):
    def get(self, request):
        all_like = Like.objects.all()
        serializer = LikeSerializer(all_like, many=True)
        return Response(serializer.data)