from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group


class SignupForm(UserCreationForm):
    role = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        empty_label="Select Role"
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "role"]
