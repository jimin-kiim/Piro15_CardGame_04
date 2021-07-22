from django import forms
from typing_extensions import Required
from django.db import models
from . import models


class LoginForm(forms.Form):
    name = models.CharField(max_length=20, verbose_name="ID")
    password = forms.CharField(widget=forms.PasswordInput)
