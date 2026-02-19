from rest_framework import viewsets
from .models import Product, Student, Prod
from .serializers import ProductSerializer, StudentSerializer, ProdSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['name', 'price']

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['name', 'category', 'price', 'stock']
    ordering_fields = ['name', 'price', 'stock']

    def get_queryset(self):
        queryset = Product.objects.all()
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        if min_price:
            queryset = queryset.filter(price__gte = min_price)
        if max_price:
            queryset = queryset.filter(price__lte = max_price)
        
        return queryset
    
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ProdViewSet(viewsets.ModelViewSet):
    queryset = Prod.objects.all()
    serializer_class = ProdSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]

    filterset_fields = ['name', 'category', 'price', 'stock']
    ordering_fields = ['name', 'price', 'stock']
    search_fields = ['name']

    def get_queryset(self):
        queryset = Prod.objects.all()
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        if min_price:
            queryset = queryset.filter(price__gte = min_price)
        if max_price:
            queryset = queryset.filter(price__lte = max_price)
        
        return queryset
