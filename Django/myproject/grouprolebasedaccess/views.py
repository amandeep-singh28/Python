from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from .forms import SignupForm


# ==================================================
# SIGNUP VIEW (Role-Based using Groups)
# ==================================================
def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            # Create user
            user = form.save()

            # Get selected role (Group)
            selected_group = form.cleaned_data['role']

            # Assign group to user
            user.groups.add(selected_group)

            # Auto login after signup
            login(request, user)

            # Redirect based on permission
            return redirect("redirect_dashboard")
    else:
        form = SignupForm()

    return render(request, "signup.html", {"form": form})


# ==================================================
# LOGIN VIEW
# ==================================================
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("redirect_dashboard")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


# ==================================================
# LOGOUT VIEW
# ==================================================
def logout_view(request):
    logout(request)
    return redirect("login")


# ==================================================
# ROLE-BASED REDIRECT
# ==================================================
@login_required
def redirect_dashboard(request):
    if request.user.has_perm('grouprolebasedaccess.view_teacher_dashboard'):
        return redirect("teacher_dashboard")

    elif request.user.has_perm('grouprolebasedaccess.view_student_dashboard'):
        return redirect("student_dashboard")

    # If no role permission assigned
    return redirect("login")


# ==================================================
# TEACHER DASHBOARD
# ==================================================
@login_required
@permission_required(
    'grouprolebasedaccess.view_teacher_dashboard',
    raise_exception=True
)
def teacher_dashboard(request):
    return render(request, "teacher_dashboard.html")


# ==================================================
# STUDENT DASHBOARD
# ==================================================
@login_required
@permission_required(
    'grouprolebasedaccess.view_student_dashboard',
    raise_exception=True
)
def student_dashboard(request):
    return render(request, "student_dashboard.html")