from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from .models import User
# from . import forms

def attack(request):
    return render(request, "users/attack.html")

def counterattack(request):
    return render(request, "users/counterattack.html")

def gameinfo(request):
    return render(request, "users/gameinfo.html")

def gamelist(request):
    return render(request, "users/gamelist.html")

def log_in(request):
    if request.method == "POST":
        form = form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            name = form.changed_data.get('name')
            password = form.cleaned_data.get('password')
            user = authenticate(name=name, password=password)

            if user is not None:
                login(request, user)
                return render(request, "users/main.html")
            else:
                return render(request, "users/login.html", {
                    'error': 'Username or Password is incorrect.',
                })
            
        else:
            return render(request, "login.html")

    form = AuthenticationForm()
    return render(request, "users/login.html", {'form':form})

def log_out(request):
    logout(request)
    return redirect(reverse("users:main"))


def main(request):
    return render(request, "users/main.html")

def ranking(request):
    users = User.objects.all()
    users.sort(key = lambda x: x.sum)
    ctx = {
        'users':users
    }
    return render(request, "users/ranking.html", ctx)