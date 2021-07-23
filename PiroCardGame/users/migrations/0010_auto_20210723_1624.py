# Generated by Django 3.2.5 on 2021-07-23 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20210723_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='card',
            field=models.CharField(choices=[('num1', '8'), ('num2', '2'), ('num3', '4'), ('num4', '5'), ('num5', '9')], max_length=10),
        ),
        migrations.AlterField(
            model_name='game',
            name='challengerCard',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='game',
            name='opponentCard',
            field=models.IntegerField(default=0),
        ),
    ]