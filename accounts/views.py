from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView
from accounts.models import User
from .forms import RegisterForm, LoginForm, ResetItDown, PasswordResetConfirmForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordChangeView
from django.core.exceptions import PermissionDenied


class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('core:congrats-page')
    
class LoginUserView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm

class ResetPassword(PasswordResetView):
    form_class = ResetItDown
    template_name = 'forgot-password.html'
    success_url = reverse_lazy('accounts:login')
    email_template_name = 'password_reset_email.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name= "new-password.html" 
    success_url = reverse_lazy('accounts:login')
    form_class = PasswordResetConfirmForm