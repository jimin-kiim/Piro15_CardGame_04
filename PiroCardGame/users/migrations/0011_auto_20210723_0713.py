# Generated by Django 3.2.5 on 2021-07-23 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20210723_0611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='game',
            name='challengerCard',
        ),
        migrations.AddField(
            model_name='game',
            name='card_list',
            field=models.CharField(default='1,2,3,4,5', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='challengeCard',
            field=models.CharField(default=1, max_length=10),
        ),
        migrations.AlterField(
            model_name='game',
            name='opponentCard',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='Card',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
