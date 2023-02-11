# Generated by Django 4.1.6 on 2023-02-10 19:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sutomGame', '0008_alter_mot_options_alter_game_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='nb_try',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='game',
            name='word',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='sutomGame.mot'),
        ),
        migrations.AlterField(
            model_name='game',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 10, 20, 27, 44, 52149)),
        ),
    ]
