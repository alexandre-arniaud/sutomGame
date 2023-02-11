import datetime as datetime
from django.contrib.auth.models import User
from django.db import models

from sutomGame.models.mot import Mot


class Game(models.Model):
    datetime = models.DateTimeField(default=datetime.datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.ForeignKey(Mot, on_delete=models.CASCADE, default=5)
    points = models.IntegerField(default=1)
    nb_try = models.IntegerField(default=1)
    is_win = models.BooleanField(default=False)


    def __str__(self):
        return f"Partie réalisée par {self.user.username} le {self.datetime} avec le mot {self.word.mot} en {self.nb_try} essais - Gagné : {self.is_win} - Points : {self.points}"
        # return f"Game {self.pk}"