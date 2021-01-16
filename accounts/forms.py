from django import forms
from accounts.models import User, UserType
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
    
    user_type = forms.ModelMultipleChoiceField(UserType.objects.all(),
        required = True,
        widget = forms.CheckboxSelectMultiple(attrs={
            'id': 'user_type',
            'class': 'usertypes'
            }),
            label='Select No')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'user_type', 'terms_agreement']

        widgets = {
            'first_name': forms.TextInput(attrs={'id': 'first_name', 'placeholder': 'Name', 'class': 'form-inputs'}),
            'last_name': forms.TextInput(attrs={'id': 'last_name', 'placeholder': 'Surname', 'class': 'form-inputs'}),
            'username': forms.TextInput(attrs={'id': 'username', 'placeholder': 'Username', 'class': 'form-inputs'}),
            'email': forms.EmailInput(attrs={'id': 'email', 'placeholder': 'Email Adress', 'class': 'form-inputs'}),
            # 'user_type': forms.CheckboxSelectMultiple(attrs={'id': 'user_type', 'class': 'usertypes'}),
            'terms_agreement': forms.CheckboxInput(attrs={'id': 'conditionAndTerms'})
        }

    # def save(self, *args, **kwargs): 
    #     user = super().save(*args, **kwargs)
    #     user_profile = User(terms_agreement=self.cleaned_data['terms_agreement'], first_name=self.cleaned_data['first_name'], last_name=self.cleaned_data['last_name'], username=self.cleaned_data['username'], email=self.cleaned_data['email']) 
    #     user_profile.save() 
    #     # user_profile.user_type.add(self.cleaned_data['user_type'])
    #     print('3-------------', self.cleaned_data['user_type'])
    #     user_profile.save()
    #     return user

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

class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'user_type']

        widgets = {
            'first_name': forms.TextInput(attrs={'id': 'first_name', 'placeholder': 'First Name',  'class': 'form-inputs'}),
            'last_name': forms.TextInput(attrs={'id': 'last_name', 'placeholder': 'Last Name',  'class': 'form-inputs'}),
            'username': forms.TextInput(attrs={'id': 'username', 'placeholder': 'Your Username',  'class': 'form-inputs'}),
            'email': forms.EmailInput(attrs={'id': 'email', 'placeholder': 'Bio',  'class': 'form-inputs'}),
            'user_type': forms.CheckboxSelectMultiple(attrs={'id': 'user_type', 'class': 'usertypes'}),
        }
