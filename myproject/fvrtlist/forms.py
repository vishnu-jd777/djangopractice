from django import forms
from . models import fvrtmodel

class fvrtform(forms.ModelForm):
    class Meta:
        model = fvrtmodel
        fields = ['name', 'fvrtactor', 'fvrtactress', 'movie','media']