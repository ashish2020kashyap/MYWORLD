from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import *

from rest_framework import status
from rest_framework.response import Response
from authentication.models import Profile




class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','user', 'gender', 'slug','birth_date','is_celeb','is_premium','verification_id','profile_picture']

