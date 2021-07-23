from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User as U
from django.urls import reverse
from .models import User, Game
from .forms import GameForm
import random
# from . import forms

def attack(request):
    option = []
    rnum = random.randint(0, 10)

    for i in range(5):
        while rnum in option:
            rnum = random.randint(0, 10)
        option.append(rnum)

    CHOICES = (
        (f'{option[0]}', f'{option[0]}'),
        (f'{option[1]}', f'{option[1]}'),
        (f'{option[2]}', f'{option[2]}'),
        (f'{option[3]}', f'{option[3]}'),
        (f'{option[4]}', f'{option[4]}'),
    )

    cardset = CHOICES[:]
    user = request.user
    print(request.user.id)
    if request.method == 'POST':
        form = GameForm(data=request.POST, cardset=cardset ,user=user)
        
        if form.is_valid():
            form.cleaned_data['challenger'] = request.user
            game = Game.objects.create(**form.cleaned_data)
            game.save()
            return render(request, 'users/gamelist.html', {'form':form})

    else:
        form = GameForm(user, cardset=cardset)
    return render(request, "users/attack.html", {'form':form})

def counterattack(request):
    return render(request, "users/counterattack.html")

def gameinfo(request, pk):
    user = User.objects.get(pk=pk)
    game = Game.objects.get(pk=pk)
    if request.method == "GET":
        ctx = {
            'user':user,
            'game':game,
        }
    else: #request method가 POST일 때: 게임 취소 클릭.
        game.delete()
        return redirect(request, "users/gamelist.html")

def gamelist(request, User, Game, pk):
    user = User.objects.get(pk=pk)
    game = Game.objects.order_by('-pk')
    if request.method == "GET":
        ctx = {
            'user':user,
            'game':game,
            'challenger':game.challenger,
        }
        return render(request, "users/gamelist.html", ctx)
    else: #method==post일때 : 게임취소클릭
        game.delete()
        return redirect("user:gamelist")


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
    users.sort(key = lambda x: x.score)
    ctx = {
        'users':users
    }
    return render(request, "users/ranking.html", ctx)