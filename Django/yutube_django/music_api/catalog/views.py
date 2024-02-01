from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from catalog.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API end point that allows users to viewed and edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_class = [permissions.AllowAny]
