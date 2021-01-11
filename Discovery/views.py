from .serializers import imageSerializer
from rest_framework.generics import (CreateAPIView)
from .models import *


class ImageCreateAPIView(CreateAPIView):
    serializer_class = imageSerializer
    queryset = MyImage.objects.all()

