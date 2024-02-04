from django.shortcuts import render
from rest_framework import generics
from blog_api.models import Post
from .serializers import PostSerializer
# Create your views here.


class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer