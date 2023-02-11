from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        pass

    def clean_username(self):
        if self.cleaned_data['username'] == '':
            self.add_error('username', 'Votre nom d\'utilisateur ne peut pas être vide !')
        return self.cleaned_data['username']

    def clean_password(self):
        if self.cleaned_data['password'] == '':
            self.add_error('password', 'Votre mot de passe ne peut pas être vide !')
        return self.cleaned_data['password']
