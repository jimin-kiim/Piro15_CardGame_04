# Generated by Django 3.2.5 on 2021-07-23 03:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_auto_20210723_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='card',
            field=models.CharField(choices=[('num1', '9'), ('num2', '1'), ('num3', '3'), ('num4', '10'), ('num5', '0')], max_length=10),
        ),
        migrations.AlterField(
            model_name='game',
            name='challenger',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='challenger', to=settings.AUTH_USER_MODEL),
        ),
    ]
