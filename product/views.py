from datetime import date
from multiprocessing import Value
from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response  import Response 
from django.views.decorators.http import require_GET
from .serializer import *
from .models import *
from product import serializer
from .serializer import ProductSerializer,CategorySerializer
from rest_framework import status
from rest_framework import filters
from . import permission
from product.permission import *


# Product views:

class Productcreate(generics.GenericAPIView):
    serializer_class = serializer.ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        # Retrieve all products
        products = Product.objects.all()
        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        # Create a new product
        permission_classes = [IsAdminOrReadOnly]
        data = request.data
        serializer = self.serializer_class(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data)
        return Response(data = serializer.errors)
    
class ProductDetail(generics.GenericAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = ProductSerializer
    
    def get(self, request, id):
        # Retrieve a specific product by ID
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(product)
        return Response(serializer.data)
    
    def put(self,request, id):
        # Update a specific product by ID
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        # Delete a specific product by ID
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Product filtering views:

class FilterProductsView(generics.GenericAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        # Retrieve all products by category
        category = self.kwargs['category']
        queryset = Product.objects.filter(category=category)

        return queryset
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
class FilterProductsByPrice(generics.ListAPIView):

    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()

        # Filter products by minimum price
        min_price = self.request.query_params.get('min_price')
        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        # Filter products by maximum price
        max_price = self.request.query_params.get('max_price')
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)   
        # to test http://127.0.0.1:8000/shop/products/?min_price=0&max_price=10


# Product search views:

class SearchProducts(generics.ListAPIView):
        serializer_class = ProductSerializer
        filter_backends = [filters.SearchFilter]
        search_fields = ['name', 'description']

        def get_queryset(self):
            queryset = Product.objects.all()
            return queryset
        

#categories:
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryProductList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = self.kwargs['id']
        return Product.objects.filter(category=category)











