from django.urls import reverse
from django.views.generic import CreateView

from sutomGame.models.mot import Mot


class MotCreateView(CreateView):
    template_name = 'mot_create_view.html'
    model = Mot
    fields = ['mot']

    def get_success_url(self):
        return reverse('admin_list_mot')