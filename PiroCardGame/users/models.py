from django.db import models
import random
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    PLAYER_CHOICES = (
        ("player1", "송경"),
        ("player2", "지수"),
        ("player3", "건모"),
        ("player4", "정훈"),
        ("player5", "지민"),
    )
    name = models.CharField(max_length=20, choices=PLAYER_CHOICES)
    sum = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Game(models.Model):
    challenger = models.ForeignKey(
        to='users.User', on_delete=models.CASCADE, related_name='challenger', null=True, default=None)
    opponent = models.ForeignKey(
        to='users.User', on_delete=models.CASCADE, related_name='opponent', null=True)
    status = models.BooleanField(default=True)  # 진행중, 게임 끝
    rule = models.BooleanField(null=True, default=True)    
    result = models.BooleanField(default=True)
    challengerCard = models.IntegerField(default=1)
    opponentCard = models.IntegerField(default=0)
