# Generated by Django 4.1.6 on 2023-02-10 17:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sutomGame', '0004_mot_alter_game_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 10, 18, 12, 40, 413317)),
        ),
        migrations.AlterField(
            model_name='mot',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]