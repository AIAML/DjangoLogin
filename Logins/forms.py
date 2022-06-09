from django import forms

from .models import Loginmodels
class LoginModelForm (forms.ModelForm):
    class Meta:
        model = Loginmodels
        fields = ['username','password']
