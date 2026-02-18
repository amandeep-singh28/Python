from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.view_student, name = 'student_list'),
    path('add/', views.add_student, name = 'student_add'),
    path('update/<int:id>/', views.update_student, name = 'student_update'),
    path('delete/<int:id>/', views.delete_student, name = 'student_delete')
]