from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from catalog.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from .models import Artist
from rest_framework import permissions
from rest_framework import authentication

class UserViewSet(viewsets.ModelViewSet):
    """
    API end point that allows users to viewed and edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_class = [permissions.AllowAny]

## requests that can be within a certain time period 
class OncePerDayUserThrottle(UserRateThrottle):
    rate = '1/day'

@api_view(['GET','POST'])
@throttle_classes([OncePerDayUserThrottle])
def hello_world(request):
    if request.method == 'POST':
        print(request.data)
        return Response({'message':'Got some data!' + str(request.data)})
    return Response({'message':'hello world!'})

class ArtistView(APIView):
    ## permissions request should be granted or denied access, set rules to who can access this view
    permission_classes = [permissions.AllowAny]
    authentication_classes = [authentication.TokenAuthentication]
    def get(self,request):
        artists  = Artist.objects.all()
        return Response(artists)
    def post(self,request):
        return Response({'data': request.data})