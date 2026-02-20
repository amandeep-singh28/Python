from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

# Product (Foreign Key -> Category)    
class Product(models.Model):
    name = models.CharField(max_length = 100)
    price = models.FloatField()
    category = models.ForeignKey(
        Category,
        on_delete = models.CASCADE,
        related_name = "products"
    )

    def __str__(self):
        return self.name

# Profile (OneToOne - User)
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        related_name = "profile"
    )
    phone = models.CharField(max_length = 15)
    address = models.TextField()

    def __str__(self):
        return self.user.username

# Order (Foreign Key - User)    
class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = "orders"
    )
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Order {self.id}"
    
# OrderItem (Through Model for ManyToMany)
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete = models.CASCADE,
        related_name = "items"
    )
    product = models.ForeignKey(
        Product,
        on_delete = models.CASCADE
    )
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
