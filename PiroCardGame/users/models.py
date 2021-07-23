from django.db import models
import random
from django.contrib.auth.models import User as U

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
    challenger = models.ForeignKey(
        to=U, on_delete=models.CASCADE, related_name='challenger', null=True, default=None)
    opponent = models.ForeignKey(
        to=U, on_delete=models.CASCADE, related_name='opponent', null=True)
    status = models.BooleanField(default=True)  # 진행중, 게임 끝
    rule = models.BooleanField(null=True, default=True)    
    result = models.BooleanField(default=True)
    challengerCard = models.CharField(choices=CHOICES, max_length=10, default=1)
    opponentCard = models.CharField(choices=CHOICES, max_length=10, null=True, default=None)
    

# class Card(models.Model):

#     option = []
#     rnum = random.randint(0, 10)

#     for i in range(5):
#         while rnum in option:
#             rnum = random.randint(0, 10)
#         option.append(rnum)

#     CHOICES = (
#         ("num1", f'{option[0]}'),
#         ("num2", f'{option[1]}'),
#         ("num3", f'{option[2]}'),
#         ("num4", f'{option[3]}'),
#         ("num5", f'{option[4]}'),
#     )

#     card = models.CharField(choices=CHOICES, max_length=10)