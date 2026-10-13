from django import forms
from .models import thalapathymodel

class thalapathyform(forms.ModelForm):
    class Meta:
        model = thalapathymodel
        fields = ['name', 'fvt']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter your name'
            }),
            'fvt': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter your favourite film'
            }),
        }