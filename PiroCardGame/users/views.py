from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.views import View
from . import forms

def attack(request):
    pass

def counterattack(request):
    pass

def gameinfo(request):
    pass

def gamelist(request):
    pass

class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, "users/login.html", {"form":form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return render(request, "users/main.html")
        return render(request, "users/main.html")


def login(request):
    return render(request, "users/login.html")

def main(request):
    return render(request, "users/main.html")

def ranking(request):
    users = User.objects.all()
    users.sort(key = lambda x: x.score)
    ctx = {
        'users':users
    }
    return render(request, "users/ranking.html", ctx)