from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
from django.views import generic

from sutomGame.forms.register import RegisterForm
from sutomGame.models.leaderboard import Leaderboard
from sutomGame.models.profile import Profile


class RegisterFormView(generic.FormView):
    template_name = 'register_form.html'
    form_class = RegisterForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        try:
            user = User.objects.create_user(
                username=username, email=email, password=password
            )
            messages.add_message(
                self.request, messages.INFO, 'Utilisateur crée avec succès !'
            )
            Leaderboard.objects.create(user=user, total_points=0)
            Profile.objects.create(user=user)
        except Exception as e:
            form.add_error(None, "Une erreur est survenu, veuillez réessauer")
            return super().form_invalid(form)
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('home')
