from django.contrib import admin
from django.urls import path
from . import views

app_name="users"

urlpatterns = [
    path('main/', name="main"),
    path('login/', views.login, name="login"),
    path('gamelist/', name="gamelist"),
    path('attack/', name="attack"), #게임하기 버튼 누르면 가는 곳
    path('gameinfo/', name="gameinfo") #게임정보 버튼 누르면 가는 곳
]
