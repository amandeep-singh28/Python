from django.shortcuts import render
from .models import Student
# Create your views here.
# def home(request, name):
#     context = {
#         'student_name' : name
#     }
#     return render(request, 'index_app.html', context)

def show_students(request):
    students = Student.objects.all()
    return render(request, "form.html", {"students": students})


    