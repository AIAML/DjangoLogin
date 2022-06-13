from django import forms

from .models import Loginmodels


class LoginModelForm(forms.ModelForm):
    class Meta:
        model = Loginmodels
        fields = ['username', 'password']


class RegisterModelForm(forms.ModelForm):
    class Meta:
        model = Loginmodels
        fields = ['username', 'password', 'email', 'fullname']
