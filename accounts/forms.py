from django import forms
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Password',
                'class' : 'form-inputs',
            }))

    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Confirm password',
                'class' : 'form-inputs',
             }))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'user_type', 'terms_agreement']

        widgets = {
            'first_name': forms.TextInput(attrs={'id': 'first_name', 'placeholder': 'Name', 'class': 'form-inputs'}),
            'last_name': forms.TextInput(attrs={'id': 'last_name', 'placeholder': 'Surname', 'class': 'form-inputs'}),
            'username': forms.TextInput(attrs={'id': 'username', 'placeholder': 'Username', 'class': 'form-inputs'}),
            'email': forms.EmailInput(attrs={'id': 'email', 'placeholder': 'Email Adress', 'class': 'form-inputs'}),
            'user_type': forms.SelectMultiple(attrs={'id': 'user_type', 'class': 'new-usertypes'}),
            'terms_agreement': forms.CheckboxInput(attrs={'id': 'conditionAndTerms'})
        }

class LoginForm(AuthenticationForm):
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Password',
                'class' : 'form-inputs',
            }))

    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'id': 'username',
                'placeholder': 'Your Username',
                'class': 'form-inputs'
            }))

    email = forms.CharField(
        widget = forms.EmailInput(
            attrs={
                'id': 'email',
                'placeholder': 'Your Email',
                'class': 'form-inputs'
            }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ResetItDown(PasswordResetForm):
    email = forms.EmailField(
        widget = forms.EmailInput(attrs={
            'placeholder': 'Your Email',
            'class': 'form-inputs',
        })
    )

class PasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'New password',
                'class' : 'form-inputs',
             }))
    
    new_password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Re-enter new password',
                'class' : 'form-inputs',
             }))

    class Meta:
        fields = ("new_password1", 'new_password2', )