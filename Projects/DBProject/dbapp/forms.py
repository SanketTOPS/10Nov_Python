from django import forms
from .models import *

class StudForm(forms.ModelForm):
    class Meta:
        model=studinfo
        fields='__all__'