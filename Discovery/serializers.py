from rest_framework import serializers

from rest_framework.serializers import (
      ModelSerializer,
)

from .models import *


class imageSerializer(ModelSerializer):
   class Meta:
      model = MyImage
      fields = [
         'model_pic'
      ]