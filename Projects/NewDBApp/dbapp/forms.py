from django import forms
from .models import *

class studForm(forms.ModelForm):
    class Meta:
        model=studInfo
        fields='__all__'