# Generated by Django 4.1.6 on 2023-02-10 16:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sutomGame', '0002_alter_game_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 10, 17, 54, 35, 44565)),
        ),
    ]
