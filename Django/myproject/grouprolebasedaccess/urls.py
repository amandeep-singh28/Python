from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path("", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.redirect_dashboard, name="redirect_dashboard"),
    path("teacher/dashboard/", views.teacher_dashboard, name="teacher_dashboard"),
    path("student/dashboard/", views.student_dashboard, name="student_dashboard"),
]
