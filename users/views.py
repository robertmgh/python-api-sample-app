from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserSerializer, AccessGroupSerializer, AccessMembershipSerializer
from .models import User, AccessGroup, AccessMembership
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

class UserList(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
    	users = User.objects.all()
    	serializer = UserSerializer(users, many=True)
    	return Response(serializer.data)
    	
class UserDetails(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
             
    
    def delete(self, request, pk, format=None):
        user = self.get_object(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class AccessGroupList(APIView):
    
    def get_list(self):
        try:
            return AccessGroup.objects.all()
        except AccessGroup.DoesNotExist:
            raise Http404
        
    def get(self, request, format=None):
        accessGroupList = self.get_list()
        serializer = AccessGroupSerializer(accessGroupList, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = AccessGroupSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AccessMembershipList(APIView):
    
    @method_decorator(cache_page(60)) #cache for each user for 1 min
    @method_decorator(vary_on_cookie)
    def get_list(self, pk):
        try:
            return AccessMembership.objects.filter(user=pk)
        except AccessMembership.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        accessGroupList = self.get_list(pk=pk)
        serializer = AccessMembershipSerializer(accessGroupList, many=True)
        return Response(serializer.data)
    
    def post(self, request, pk, format=None):
        serializer = AccessMembershipSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
