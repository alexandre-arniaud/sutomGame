from django.contrib.auth.models import User
from django.db import models

from sutomGame.models.game import Game


class Leaderboard(models.Model):
    position = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_points = models.IntegerField()
    total_games = models.IntegerField(default=0)

    def __str__(self):
        return f" {self.user.username.upper()} est en {self.position}e position avec {self.total_points} points"
        # return f"Game {self.pk}"

    def create_leaderboard(request):
        users = User.objects.all()
        leaderboards = []
        for user in users:
            games = Game.objects.filter(user=user)
            games_count = Game.objects.filter(user=user).count()
            total_points = sum(game.points for game in games)
            Leaderboard.objects.create(user=user, total_points=total_points)
            leaderboards.append(Leaderboard(user=user, total_points=total_points, total_games=games_count))
        Leaderboard.objects.all().delete()
        Leaderboard.objects.bulk_create(sorted(leaderboards, key=lambda x: x.total_points, reverse=True), ignore_conflicts=True)
