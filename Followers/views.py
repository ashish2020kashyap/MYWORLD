from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import FollowerSerializer,FollowingSerializer
from .models import *
from django.http import HttpResponse
from django.http import Http404


class all_follow(APIView):
    def get(self, request):
        print(request.data)
        all_follow = Follower.objects.all()
        serializer = FollowerSerializer(all_follow, many=True)
        return Response(serializer.data)


    def post(self, request):
        print(request.data)
        serializer = FollowerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class followrud(APIView):

    def get_object(self, pk):
        try:
            return Follower.objects.get(pk=pk)
        except Follower.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pro = self.get_object(pk)
        serializer = FollowerSerializer(pro)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        single_follow = self.get_object(pk)
        serializer = FollowerSerializer(single_follow, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk, format=None):
        single_follow_delete = self.get_object(pk)
        single_follow_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class follow(APIView):

    def get(self, request,pk):
        follow_1 = Follower.objects.all()
        follow_2= follow_1.filter(myfollow=pk)
        follow_3 = follow_1.filter(myfollow=pk).count()
        print(follow_3)
        serializer = FollowerSerializer(follow_2, many=True)
        return Response(serializer.data)



class all_following(APIView):
    def get(self, request):
        print(request.data)
        all_following = Following.objects.all()
        serializer = FollowingSerializer(all_following, many=True)
        return Response(serializer.data)


    def post(self, request):
        print(request.data)
        serializer = FollowingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class followingrud(APIView):

    def get_object(self, pk):
        try:
            return Following.objects.get(pk=pk)
        except Following.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pro = self.get_object(pk)
        serializer = FollowingSerializer(pro)
        return Response(serializer.data)




    def delete(self, request, pk, format=None):
        single_following_delete = self.get_object(pk)
        single_following_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class followpost(APIView):
    def post(self, request,pk):
        serializer = FollowerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class following(APIView):

    def get(self, request,pk):
        follow_1 = Follower.objects.all()
        follow_2= follow_1.filter(myfollow=pk)
        follow_3 = follow_1.filter(myfollow=pk).count()
        print(follow_3)
        serializer = FollowerSerializer(follow_2, many=True)
        return Response(serializer.data)



class countfollow(APIView):

    def get(self, request,pk):
        follow_1 = Follower.objects.all()
        follow_2= follow_1.filter(myfollow=pk).count()
        res={'totalfollowers':follow_2}
        return Response(res)


