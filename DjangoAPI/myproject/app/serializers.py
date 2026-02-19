from rest_framework import serializers
from .models import Product, Student, Prod

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prod
        fields = '__all__'