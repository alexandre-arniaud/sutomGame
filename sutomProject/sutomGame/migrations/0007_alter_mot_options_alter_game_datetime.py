# Generated by Django 4.1.6 on 2023-02-10 17:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sutomGame', '0006_alter_game_datetime'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mot',
            options={'ordering': ['mot']},
        ),
        migrations.AlterField(
            model_name='game',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 10, 18, 51, 45, 781296)),
        ),
    ]