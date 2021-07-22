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
    choice = models.ForeignKey(to='users.Card', on_delete=models.CASCADE)
    sum = models.IntegerField()
    result = models.BooleanField()

    def __str__(self):
        return self.name


class Game(models.Model):

    challenger = models.ForeignKey(to='users.User', on_delete=models.CASCADE, related_name='challenger')
    opponent = models.ForeignKey(to='users.User', on_delete=models.CASCADE, related_name='opponent')
    # challenger_choice = models.ForeignKey(to='users.Card')
    # opponent_choice = models.ForeignKey(to='users.Card')
    status = models.IntegerField()
    # result = models.BooleanField()


class Card(models.Model):

    option = []
    rnum = random.randint(0, 10)

    for i in range(5):
        while rnum in option:
            rnum = random.randint(0, 10)
        option.append(rnum)

    CHOICES = (

        ("num1", ''),
        ("num2", ''),
        ("num3", ''),
        ("num4", ''),
        ("num5", ''),

    )
