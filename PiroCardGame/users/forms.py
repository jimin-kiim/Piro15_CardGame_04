from django import forms
from django.db import models


class LoginForm(forms.Form):
    name = models.CharField(max_length=20, verbose_name="ID")
    password = forms.CharField(widget=forms.PasswordInput)
