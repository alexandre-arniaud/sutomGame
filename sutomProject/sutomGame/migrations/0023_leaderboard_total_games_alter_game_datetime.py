# Generated by Django 4.1.6 on 2023-02-11 13:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sutomGame', '0022_alter_game_datetime_alter_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaderboard',
            name='total_games',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='game',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 14, 38, 58, 110566)),
        ),
    ]