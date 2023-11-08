from django.http import Http404
from rest_framework import viewsets

from .serializers import UserSerializer
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
#def detail(request, user_id):
#    try:
#        user = User.objects.get(pk=user_id)
#    except User.DoesNotExist:
#        raise Http404("User does not exist")
#    return HttpResponse(user)
