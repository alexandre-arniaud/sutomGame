from django.db.models import Sum
from django.views.generic import TemplateView

from sutomGame.models.game import Game
from sutomGame.models.leaderboard import Leaderboard
from sutomGame.models.mot import Mot


class AdminPanelView(TemplateView):
    template_name = 'admin_panel.html'
    model = Leaderboard, Game, Mot

    def get_context_data(self, **kwargs):
        all_total_points = Game.objects.aggregate(Sum('points'))['points__sum']
        count_users = Leaderboard.objects.all().count()
        count_played_games = Game.objects.all().count()
        count_words = Mot.objects.all().count()
        context = super().get_context_data(**kwargs)
        context['all_total_points'] = all_total_points
        context['count_users'] = count_users
        context['count_played_games'] = count_played_games
        context['count_words'] = count_words
        return context