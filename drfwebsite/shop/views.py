from django import views
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView, status
from rest_framework.pagination import PageNumberPagination

from .serializers import ProductSerialaizer
from .models import Product


class ProductListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 10000

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerialaizer

class ProductAPIList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialaizer
    pagination_class = ProductListPagination

class ProductAPIUpdate(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialaizer

class ProductAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialaizer