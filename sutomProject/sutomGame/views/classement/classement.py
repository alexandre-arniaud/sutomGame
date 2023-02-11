from django.views.generic import ListView

from sutomGame.models.leaderboard import Leaderboard


class ClassementListView(ListView):
    template_name = 'classement_list_view.html'
    model = Leaderboard

    def get_context_data(self, **kwargs):
        items = Leaderboard.objects.all().order_by('-total_points')
        context = super().get_context_data(**kwargs)
        context['items'] = items
        return context
