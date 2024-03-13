from django.shortcuts import render
from django.http import HttpRequest, JsonResponse, response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

posts = [
    {
        "id":1,
        "title":"Hello World",
        "body":"Hello World",
    },
    {
        "id":2,
        "title":"Hello World",
        "body":"Hello World",
    },
    {
        "id":3,
        "title":"Hello World",
        "body":"Hello World",
    }
]

@api_view(http_method_names=['GET',"POST"])
def homepage(request:HttpRequest):
    if request.method == "POST":
        data = request.data
        response ={"message":"Hello World","data":data}
        return JsonResponse(data=response,status=status.HTTP_201_CREATED)
    response ={"message":"Hello World"}
    return JsonResponse(data=response,status=status.HTTP_200_OK)

@api_view(http_method_names=["GET"])
def list_posts(request:HttpRequest):
    return Response(data=posts,status=status.HTTP_200_OK)

@api_view(http_method_names=["GET"])
def post_detail(request:HttpRequest,post_id:int):
    post = posts[post_id]
    
    if post:
        return Response(data=post,status=status.HTTP_200_OK)
    
    return Response(data={"error":"Post not found"},status=status.HTTP_404_NOT_FOUND)