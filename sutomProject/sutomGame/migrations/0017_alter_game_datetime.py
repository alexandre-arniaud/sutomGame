# Generated by Django 4.1.6 on 2023-02-11 01:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sutomGame', '0016_alter_game_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 2, 14, 24, 774823)),
        ),
    ]
