from django import forms
from typing_extensions import Required
from django.db import models


class LoginForm(forms.Form):
    name = models.CharField(max_length=20, verbose_name="ID")
    email = models.EmailField(verbose_name="E-mail")
    password = forms.CharField(widget=forms.PasswordInput)