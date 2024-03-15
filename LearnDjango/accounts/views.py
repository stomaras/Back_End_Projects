from django.shortcuts import render
from .serializers import SignUpSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.request import Request
from django.http import HttpRequest, JsonResponse, response

# Create your views here.

class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    
    def post(self, request:HttpRequest):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            
            response = {
                "message": "User created successfully",
                "data":serializer.data,
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)