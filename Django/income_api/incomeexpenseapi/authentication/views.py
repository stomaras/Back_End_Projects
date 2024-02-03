from django.shortcuts import render
from rest_framework import generics, status
# Create your views here.
from .serializers import RegisterSerializer
from rest_framework.response import Response

class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer


    def post(self, request):
        user=request.data
        serializer=RegisterSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data
        print("user data", user_data)

        return Response(user_data, status=status.HTTP_201_CREATED)
