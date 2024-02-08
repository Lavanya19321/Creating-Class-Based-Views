from django import forms
from app.models import *

class schoolform(forms.ModelForm):
    class Meta:
        model=School
        fields='__all__'