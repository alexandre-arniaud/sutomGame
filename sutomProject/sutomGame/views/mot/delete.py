from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import DeleteView
from django.urls import reverse
from sutomGame.models.mot import Mot


class MotDeleteView(DeleteView):
    template_name = 'mot_delete_view.html'
    model = Mot

    def get_success_url(self):
        return reverse('admin_list_mot')

    def post(self, request, *args, **kwargs):
        print("TEST")
        messages.all_messages = []
        messages.add_message(self.request, messages.SUCCESS, 'Suppression effectuée avec succès !')
        return HttpResponseRedirect(reverse('admin_list_mot'))
