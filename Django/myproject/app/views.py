from django.shortcuts import render

# Create your views here.
def home(request, name):
    context = {
        'student_name' : name
    }
    return render(request, 'index_app.html', context)