from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import  reverse
from django.views.generic import UpdateView
from sutomGame.models.mot import Mot


class MotUpdateView(UpdateView):
    template_name = 'mot_update_view.html'
    model = Mot
    fields = ['mot']

    def get_success_url(self):
        return reverse('admin_list_mot')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        messages.all_messages = []
        messages.add_message(self.request, messages.SUCCESS, 'Modification effectuée avec succès !')
        return HttpResponseRedirect(reverse('admin_list_mot'))

