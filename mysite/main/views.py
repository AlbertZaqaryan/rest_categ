from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product
# Create your views here.


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
