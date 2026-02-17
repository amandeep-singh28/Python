from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied

# Login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")

# Common Dashboard Redirect
@login_required
def dashboard(request):
    if request.user.is_staff:
        return redirect("teacher_dashboard")
    else:
        return redirect("student_dashboard")

# Teacher dashboard
@login_required
def teacher_dashboard(request):
    if not request.user.is_staff:
        raise PermissionDenied
    return render(request, "teacher_dashboard.html")

# Student Dashboard
@login_required
def student_dashboard(request):
    if request.user.is_staff:
        raise PermissionDenied
    return render(request, "student_dashboard.html")

# Permission based view
@permission_required("auth.view_user")
def view_users(request):
    return render(request, "view_users.html")