from django.db import models
import random


class User(models.Model):
    PLAYER_CHOICES = (
        ("player1", "송경"),
        ("player2", "지수"),
        ("player3", "건모"),
        ("player4", "정훈"),
        ("player5", "지민"),
    )
    name = models.CharField(max_length=20, choices=PLAYER_CHOICES)
    choice = models.ForeignKey(to='users.Card', on_delete=models.CASCADE, null=True)
    sum = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Game(models.Model):
    challenger = models.ForeignKey(
        to='users.User', on_delete=models.CASCADE, related_name='challenger', null=True)
    opponent = models.ForeignKey(
        to='users.User', on_delete=models.CASCADE, related_name='opponent', null=True)
    status = models.IntegerField(null=True)  # 진행중, 게임 끝
    rule = models.BooleanField(null=True)    
    result = models.BooleanField() 


class Card(models.Model):

    option = []
    rnum = random.randint(0, 10)

    for i in range(5):
        while rnum in option:
            rnum = random.randint(0, 10)
        option.append(rnum)

    CHOICES = (
        ("num1", f'{option[0]}'),
        ("num2", f'{option[1]}'),
        ("num3", f'{option[2]}'),
        ("num4", f'{option[3]}'),
        ("num5", f'{option[4]}'),
    )

    card = models.CharField(choices=CHOICES, max_length=10)