from django.shortcuts import render
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import connection
from pygments import highlight
# Create your views here.
from pygments.formatters import TerminalFormatter
from pygments.lexers import SqlLexer
from sqlparse import format

from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer

class CategoryViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing categories.
    """
    
    queryset = Category.objects.all()
    
    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
    
class BrandViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing brands.
    """
    
    queryset = Brand.objects.all()
    print(connection.queries)
    
    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
class ProductViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing all products.
    """
    
    queryset = Product.objects.all()
    
    
    
    lookup_field = "slug"
    
    def retrieve(self, request, slug=None):
        serializer = ProductSerializer(self.queryset.filter(slug=slug).select_related("category", "brand"), many=True)
        data = Response(serializer.data)
        
        q = list(connection.queries)
        print(len(q))
        for qq in q:
            sqlformatted = format(str(qq["sql"]), reindent=True)
            print(highlight(sqlformatted, SqlLexer(), TerminalFormatter()))
        
        # x = self.queryset.filter(slug=slug)
        # sqlformatted = format(str(x.query), reindent=True)
        # print(highlight(sqlformatted, SqlLexer(), TerminalFormatter()))
        
        return data
    
    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    @action(
        methods=["get"], 
        detail=False, 
        url_path=r'category/(?P<category>\w+)/all',
        url_name="all",
    )
    def list_product_by_category(self, request, category=None):
        """
        An endpoint to return products by category
        """
        serializer = ProductSerializer(self.queryset.filter(category__name=category), many=True)
        return Response(serializer.data)
        