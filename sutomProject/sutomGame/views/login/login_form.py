from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic

from sutomGame.forms.login import LoginForm


class LoginFormView(generic.FormView):
    template_name = 'login_form.html'
    form_class = LoginForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)
            return redirect('home')
        else:
            error_message = 'Email ou Mot de passe incorrect'
            return render(self.request, 'login_form.html', {'form': form, 'error_message': error_message})

    def get_success_url(self):
        return reverse('home')

    def logout(self):
        logout(self.request)
        return redirect('home')
