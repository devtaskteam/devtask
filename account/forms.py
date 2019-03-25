from django import forms
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User

from .models import Profile


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Введите пароль ещё раз', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']
