from django.http import HttpResponse, request
from django.shortcuts import render
def say_hello(request):
    return HttpResponse("Hello World")

def say_goodmorning(request):
    return render(request, 'index.html')