from django import forms
from .models import subscribe

class SubscribeTableForm(forms.ModelForm):
    class Meta:
        model = subscribe
        fields ='__all__'