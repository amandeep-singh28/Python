from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm


# 1️⃣ View Product List
def product_list(request):
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})


# 2️⃣ Add Product
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()

    return render(request, "add_product.html", {"form": form})


# 3️⃣ Update Stock
def update_stock(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)

    return render(request, "update_stock.html", {"form": form})
