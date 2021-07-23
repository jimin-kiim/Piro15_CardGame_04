from django.contrib import admin
from django.urls import path
from . import views

app_name="users"

urlpatterns = [
    path('', views.main, name="main"),
    path('login/', views.log_in, name="login"),
    path('<int:pk>/gamelist/', views.gamelist, name="gamelist"),
    path('attack/', views.attack, name="attack"), #게임하기 버튼 누르면 가는 곳
    path('gameinfo/', views.gameinfo, name="gameinfo"), #게임정보 버튼 누르면 가는 곳
    path('ranking/', views.ranking, name="ranking"),
]
