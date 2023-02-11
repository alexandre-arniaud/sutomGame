from django.contrib import admin

from sutomGame.models.game import Game
from sutomGame.models.leaderboard import Leaderboard
from sutomGame.models.mot import Mot
from sutomGame.models.profile import Profile

admin.site.register(Game)
admin.site.register(Mot)
admin.site.register(Leaderboard)
admin.site.register(Profile)