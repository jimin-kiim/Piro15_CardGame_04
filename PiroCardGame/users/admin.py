from django.contrib import admin
from django.db import models
from . import models

@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Game)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Card)
class CustomUserAdmin(admin.ModelAdmin):
    pass