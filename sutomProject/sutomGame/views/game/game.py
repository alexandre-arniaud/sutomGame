from random import choice

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from sutomGame.forms.game import GameForm
from sutomGame.models.game import Game
from sutomGame.models.leaderboard import Leaderboard
from sutomGame.models.mot import Mot


@method_decorator(login_required, name='dispatch')
class GameView(TemplateView):
    template_name = 'game.html'

    def get_context_data(self, **kwargs):
        form = GameForm(self.request.POST or None)
        if self.request.method == 'POST' and form.is_valid():
            form.save()

        context = super().get_context_data(**kwargs)
        context['game'] = Game.objects.all()
        context['mot'] = choice(Mot.objects.all())
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        Leaderboard.create_leaderboard(request)
        return redirect('home')
