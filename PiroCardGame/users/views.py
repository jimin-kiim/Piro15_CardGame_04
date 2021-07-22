from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from .models import User

def attack(request):
    pass

def counterattack(request):
    pass

def gameinfo(request):
    pass

def gamelist(request):
    pass

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