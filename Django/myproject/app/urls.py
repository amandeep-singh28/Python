from django.urls import path
from . import views

urlpatterns = [

    path('student/<str:name>/',views.home, name = 'student')

]