from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import CommentSerializer
from .models import *
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated

class all_comment(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        all_comment = Comment.objects.all()
        serializer = CommentSerializer(all_comment, many=True)
        return Response(serializer.data)