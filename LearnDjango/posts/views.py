from django.shortcuts import render
from django.http import HttpRequest, JsonResponse, response
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404


@api_view(http_method_names=['GET',"POST"])
def homepage(request:HttpRequest):
    if request.method == "POST":
        data = request.data
        response ={"message":"Hello World","data":data}
        return JsonResponse(data=response,status=status.HTTP_201_CREATED)
    response ={"message":"Hello World"}
    return JsonResponse(data=response,status=status.HTTP_200_OK)

class PostListCreateView(APIView):
    """
    A view for creating and listing posts
    """
    serializer_class = PostSerializer
    def get(self, request:HttpRequest,*args,**kwargs):
        posts = Post.objects.all()
        
        serializer = self.serializer_class(instance=posts,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request:HttpRequest,*args,**kwargs):
        data = request.data
        
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            
            response = {
                "message":"Post Created Successfully",
                "data":serializer.data,
            }
            
            return Response(data=response,status=status.HTTP_201_CREATED)

@api_view(http_method_names=["GET"])
def post_detail(request:HttpRequest,post_id:int):
    post = get_object_or_404(Post,pk=post_id)
    
    serializer = PostSerializer(instance=post)
    
    response = {"message":"post","data":serializer.data}
    
    return Response(data=response,status=status.HTTP_200_OK)


class PostRetrieveUpdateDeleteView(APIView):
    serializer_class = PostSerializer
    
    def get(self, request:HttpRequest,post_id:int):
        post = get_object_or_404(Post,pk=post_id)
        serializer = self.serializer_class(instance=post)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def put(self, request:HttpRequest,post_id:int):
        post = get_object_or_404(Post,pk=post_id)
        data = request.data
        serializer = self.serializer_class(instance=post,data=data)
        
        if serializer.is_valid():
            serializer.save()
            
            response = {
                "message":"Post Updated Successfully",
                "data":serializer.data,
            }
            
            return Response(data=response,status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request:HttpRequest,post_id:int):
        post = get_object_or_404(Post,pk=post_id)
        post.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)