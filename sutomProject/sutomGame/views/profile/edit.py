from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from sutomGame.forms.profile_update import ProfileUpdateForm
from sutomGame.forms.user_update import UserUpdateForm


class ProfileView(TemplateView):
    template_name = 'profile.html'
    user = User

    @login_required
    def get_context_data(self, **kwargs):
        u_form = UserUpdateForm(instance=self.request.user)
        p_form = ProfileUpdateForm(instance=self.request.user.profile)

        context = {
            'u_form': u_form,
            'p_form': p_form
        }

        return context

    def post(self, request, *args, **kwargs):
        print(self.request.method)
        if self.request.method == 'POST':
            u_form = UserUpdateForm(self.request.POST, instance=self.request.user)
            p_form = ProfileUpdateForm(self.request.POST,
                                       self.request.FILES,
                                       instance=self.request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(self.request, f'Votre compte a été mis à jour avec succès !')
                return redirect('profile')  # Redirect back to profile page

