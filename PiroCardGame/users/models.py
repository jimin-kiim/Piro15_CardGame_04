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
    choice = models.ForeignKey(to='users.Card', on_delete=models.SET_NULL)
    sum = models.IntegerField(default=0)
    result = models.BooleanField()#승패여부

    def __str__(self):
        return self.name


class Game(models.Model):

    challenger = models.ForeignKey(
        to='users.User', on_delete=models.CASCADE, related_name='challenger')
    opponent = models.ForeignKey(
        to='users.User', on_delete=models.CASCADE, related_name='opponent')
    # challenger_choice = models.ForeignKey(to='users.Card')
    # opponent_choice = models.ForeignKey(to='users.Card')
    status = models.IntegerField()#진행중, 게임 끝
    rule=models.BooleanField()


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

    card = models.IntegerField(choices=CHOICES)