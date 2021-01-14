from django import forms
from .models import BetaUsers

class SignUpForBetaForm(forms.ModelForm):
    class Meta:
        model = BetaUsers
        fields = ['full_name', 'company', 'email',]

        widgets = {
            'full_name': forms.TextInput(attrs={'id': 'full_name', 'placeholder': 'Full Name', 'class': 'form-inputs'}),
            'company': forms.TextInput(attrs={'id': 'company', 'placeholder': 'Company', 'class': 'form-inputs'}),
            'email': forms.EmailInput(attrs={'id': 'email', 'placeholder': 'Email Adress', 'class': 'form-inputs'}),
        }