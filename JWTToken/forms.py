from django import forms
from django.contrib.auth.forms import UserCreateForm
from django.contrib.auth.models import User

class RegisterForm(UserCreateForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        