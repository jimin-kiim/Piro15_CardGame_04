from django.contrib import admin
from . import models

@admin.register(models.Game)
class CustomUserAdmin(admin.ModelAdmin):
    pass

