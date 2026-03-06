from django import forms
from .models import *

class SignupForm(forms.ModelForm):
    class Meta:
        model=userSignup
        fields='__all__'