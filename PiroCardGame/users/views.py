from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User as U
from django.urls import reverse
from .models import User
from .models import Game
import random

from django.contrib.auth.models import User as U
# from . import forms

def attack(request):
    if request.method == "POST":
        challenger = request.user
        opponent = request.POST["opponent"]
        challengerCard = request.POST["cardset"]
        realOpponent = User.objects.get(username=opponent)
        game = Game(challenger=challenger, opponent=realOpponent, challengerCard=challengerCard)
        game.save()
        return redirect("users:main")

    else:
        cardset = []
        cards = random.sample(range(1,10),5)
        
        user_all = User.objects.exclude(id=request.user.id)
        ctx = {
            "user_all": user_all,
            "cardset": cards,
        }
        return render(request, "users/attack.html", ctx)

def counterattack(request):
   if request.method == "GET":
       cardset = []
       for _ in range(5):
           cardSelect = random.randint(1, 10)
           cardset.append(cardSelect)
        return render(request, "users/counterattack.html")
    else: #post방식일 때 : 반격하기 버튼 누른경우. : 게임 결과창으로 이동 
        return render(request, "users/attack.html", ctx)

def gameinfo(request, pk):
    game = get_object_or_404(Game, pk=pk)
    ctx = {"game": game}
    return render(request, "users/gameinfo.html", ctx)

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
    user = request.user #로그인 된 사람    
    games = Game.objects.all() #game 모델
    ctx={'user':user,'games':games}
    return render(request, "users/gamelist.html",ctx)
    

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
    users = User.objects.all()
    ctx={'users':users}

def ranking(request):
    users = list(User.objects.all().order_by('sum'))
    ctx = {
        'users':users
    }
    return render(request, "users/ranking.html", ctx)

def delete(request,pk):
    game=Game.objects.get(id=pk)
    game.delete()
    return redirect('users:gamelist') 