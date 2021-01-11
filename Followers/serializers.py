from authentication.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import *

from rest_framework import status
from rest_framework.response import Response





class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ['id','myfollow']


class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = ['id','myfollowing']


