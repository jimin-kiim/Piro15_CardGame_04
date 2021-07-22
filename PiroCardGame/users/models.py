from django.db import models

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

    def __str__(self):
        return self.name


class Game(models.Model):
    NUM_CHOICES = []
    rnum = random.randint(0, 10)

    for i in range(5):
        while rnum in NUM_CHOICES:
            rnum = random.randint(0, 10)
        NUM_CHOICES.append(rnum)

    challenger = models.ForeignKey(
        to='users.User', on_delete=models.CASCADE, related_name='game')
    opponent = models.ForeignKey(
        to='users.User', on_delete=models.CASCADE, related_name='game')

    challenger_choice = models.IntegerField(choices=NUM_CHOICES)
    opponent_choice = models.IntegerField(choices=NUM_CHOICES)

    status = models.IntegerField()
    result = models.BooleanField()

# 게임 점수는 +-(본인의 선택 숫자)
# 게임 승자 기준은 2가지 랜덤 : 숫자가 큰 사람 / 작은 사람
class Game(models.Model):
    pass
