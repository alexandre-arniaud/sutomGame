from django.views import generic

from sutomGame.models.leaderboard import Leaderboard


class IndexView(generic.TemplateView):
    template_name = 'home.html'
    model = Leaderboard

    def get_context_data(self, **kwargs):
        items = Leaderboard.objects.all().order_by('-total_points')
        context = super().get_context_data(**kwargs)
        context['items'] = items
        return context