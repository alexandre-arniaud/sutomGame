from django import forms

from sutomGame.models.game import Game


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['word', 'user', 'nb_try', 'points', 'is_win']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['word'].widget.attrs.update({'class': 'form-control'})
        self.fields['user'].widget.attrs.update({'class': 'form-control'})
        self.fields['nb_try'].widget.attrs.update({'class': 'form-control'})
        self.fields['points'].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        pass

    def clean_word(self):
        if self.cleaned_data['word'] == '':
            self.add_error('word', 'Votre word ne peut pas être vide !')
        return self.cleaned_data['word']

    def clean_user(self):
        if self.cleaned_data['user'] == '':
            self.add_error('user', 'Votre user ne peut pas être vide !')
        return self.cleaned_data['user']

    def clean_nb_try(self):
        if self.cleaned_data['nb_try'] == '':
            self.add_error('nb_try', 'Votre nb essais ne peut pas être vide !')
        return self.cleaned_data['nb_try']

    def clean_points(self):
        if self.cleaned_data['points'] == '':
            self.add_error('points', 'Votre points ne peut pas être vide !')
        return self.cleaned_data['points']
