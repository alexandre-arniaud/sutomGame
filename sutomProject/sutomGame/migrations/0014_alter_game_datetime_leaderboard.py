# Generated by Django 4.1.6 on 2023-02-11 00:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sutomGame', '0013_rename_is_finished_game_is_win_game_points_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 1, 44, 23, 237846)),
        ),
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('position', models.IntegerField(primary_key=True, serialize=False)),
                ('total_points', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sutomGame.game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
