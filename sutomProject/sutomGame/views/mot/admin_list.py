from django.views.generic import ListView

from sutomGame.models.mot import Mot


class MotListView(ListView):
    template_name = 'mot_list_view.html'
    model = Mot
