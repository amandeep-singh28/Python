from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 100)
    price = models.FloatField()

class Student(models.Model):
    student_name = models.CharField(max_length = 100)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length = 100)
    course = models.CharField(max_length = 100)

class Prod(models.Model):
    name = models.CharField(max_length = 200)
    category = models.CharField(max_length = 200)
    price = models.FloatField()
    stock = models.PositiveIntegerField()