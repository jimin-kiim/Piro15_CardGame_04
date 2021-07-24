from django.db.models import fields
from django.db.models.fields import CharField
from django import forms
from django.db import models
from django.forms.fields import ChoiceField
from django.forms.models import ModelChoiceField, fields_for_model
from users.models import Game
from django.contrib.auth.models import User
import random

class LoginForm(forms.Form):
    name = models.CharField(max_length=20, verbose_name="ID")
    email = models.EmailField(verbose_name="E-mail")
    password = forms.CharField(widget=forms.PasswordInput)

