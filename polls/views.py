from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import User
from rest_framework.response import Response

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

#class UserViewSet(APIView):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
    
#def detail(request, user_id):
#    try:
#        user = User.objects.get(pk=user_id)
#    except User.DoesNotExist:
#        raise Http404("User does not exist")
#    return HttpResponse(user)
