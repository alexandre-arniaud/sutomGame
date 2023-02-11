from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", min_length=5, max_length=100,)
    email = forms.EmailField(label="E-mail")
    password = forms.CharField(label="Mot de passe",
                               min_length=5, max_length=100,
                               widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        pass

    def clean_username(self):
        if self.cleaned_data['username'] == '':
            self.add_error('username', 'Votre nom d\'utilisateur ne peut pas être vide !')
        return self.cleaned_data['username']

    def clean_email(self):
        if self.cleaned_data['email'] == '':
            self.add_error('email', 'Votre e-mail ne peut pas être vide !')
        return self.cleaned_data['email']

    def clean_password(self):
        if self.cleaned_data['password'] == '':
            self.add_error('password', 'Votre mot de passe ne peut pas être vide !')
        return self.cleaned_data['password']
