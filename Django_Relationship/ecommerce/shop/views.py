from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer, ProductSerializer, OrderItemSerializer, OrderSerializer, ProfileSerializer
from .models import Category, OrderItem, Product, Order, Profile
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','name']

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'price', 'category']
        

class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
