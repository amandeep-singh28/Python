from django.http import HttpResponse, request

def say_hello(request):
    return HttpResponse("Hello World")

def say_goodmorning(request):
    return HttpResponse("Good Morning")