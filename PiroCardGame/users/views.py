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
    if request.method == "POST":
        challenger = request.user
        opponent = request.POST["opponent"]
        challengerCard = request.POST["cardset"]
        realOpponent = U.objects.get(username=opponent)
        game = Game(challenger=challenger, opponent=realOpponent, challengerCard=challengerCard)
        game.save()
        return redirect("users:gamelist")

    else:
        cardset = []
        cards = random.sample(range(1,10),5)
        
        user_all = U.objects.exclude(id=request.user.id)
        # user_all.remove(request.user)
        ctx = {
            "user_all": user_all,
            "cardset": cards,
        }
        return render(request, "users/attack.html", ctx)

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
        # game.delete()
        return redirect(request, "users/gamelist.html")

# def gamelist(request, User, Game, pk):
#     user = User.objects.get(pk=pk)
#     game = Game.objects.order_by('-pk')
#     if request.method == "GET":
#         ctx = {
#             'user':user,
#             'game':game,
#             'challenger':game.challenger,
#         }
#         return render(request, "users/gamelist.html", ctx)
#     else: #method==post일때 : 게임취소클릭
#         game.delete()
#         return redirect("user:gamelist")

def gamelist(request):
    return render(request, "users/main.html")

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
    users = User.objects.all().order_by('sum')
    ctx = {
        'users':users
    }
    return render(request, "users/ranking.html", ctx)