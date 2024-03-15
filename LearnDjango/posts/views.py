from django.shortcuts import render
from django.http import HttpRequest, JsonResponse, response
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer