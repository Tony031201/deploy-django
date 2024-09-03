from django import forms
from .models import subscribe

class SubscribeTableForm(forms.ModelForm):
    class Meta:
        model = subscribe
        fields = ['name','email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
        }