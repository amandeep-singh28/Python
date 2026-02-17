from django.db import models

class RolePermission(models.Model):
    class Meta:
        permissions = [
            ("view_teacher_dashboard", "Can view teacher dashboard"),
            ("view_student_dashboard", "Can view student dashboard"),
        ]
