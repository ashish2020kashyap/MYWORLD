from authentication.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import *

from rest_framework import status
from rest_framework.response import Response



class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']


