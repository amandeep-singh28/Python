from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("add/", views.add_product, name="add_product"),
    path("update/<int:pk>/", views.update_stock, name="update_stock"),
]
