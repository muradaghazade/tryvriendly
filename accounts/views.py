from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView
from accounts.models import User
from .forms import RegisterForm, LoginForm, ResetItDown, PasswordResetConfirmForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordChangeView
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail


class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('core:congrats-page')

    def form_valid(self, form):
        user_email = form.instance.email
        send_mail('subject', 'body of the message', 'tech.academy.user2@gmail.com', [user_email,])
        # form.instance.is_sell = False
        # form.instance.product = self.get_object()
        # print(form.instance.price)
        form.save()
        return super().form_valid(form)
    
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