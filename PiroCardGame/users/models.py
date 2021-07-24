from django.db import models
import random
from django.contrib.auth.models import AbstractUser


# FIXME: AbstractUser -> AbstractBaseUser
class User(AbstractUser):
    
    sum = models.IntegerField(default=0) # FIXME: sum 변수명 바꿔주세요!

    def __str__(self):
        return self.username


    # 앱 쪼개기
class Game(models.Model):
    challenger = models.ForeignKey(
        to='users.User', on_delete=models.CASCADE, related_name='challenger', null=True, default=None) # Lazy relation (1) 상호참조 (2) 자기참조 
    opponent = models.ForeignKey(
        to='users.User', on_delete=models.CASCADE, related_name='opponent', null=True)
    status = models.BooleanField(default=True)  # 진행중, 게임 끝
    rule = models.BooleanField(null=True, default=True)    
    result = models.BooleanField(default=True)
    challenger_card = models.IntegerField(default=1)
    opponent_card = models.IntegerField(default=0) # camelCase snake_case # default -> 유효한 값 
