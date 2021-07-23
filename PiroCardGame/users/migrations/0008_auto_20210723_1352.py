# Generated by Django 3.2.5 on 2021-07-23 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210723_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='card',
            field=models.CharField(choices=[('num1', '9'), ('num2', '6'), ('num3', '2'), ('num4', '0'), ('num5', '5')], max_length=10),
        ),
        migrations.AlterField(
            model_name='game',
            name='challengerCard',
            field=models.CharField(choices=[('1', '1'), ('9', '9'), ('0', '0'), ('7', '7'), ('10', '10')], default=1, max_length=10),
        ),
        migrations.AlterField(
            model_name='game',
            name='opponentCard',
            field=models.CharField(choices=[('1', '1'), ('9', '9'), ('0', '0'), ('7', '7'), ('10', '10')], default=None, max_length=10, null=True),
        ),
    ]
