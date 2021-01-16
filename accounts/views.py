from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView
from accounts.models import User
from .forms import RegisterForm, LoginForm, ResetItDown, PasswordResetConfirmForm, UpdateProfileForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordChangeView
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate


def usersignup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            user_types = request.POST.getlist('user_type')
            user.user_type.set(user_types)
            user.save()

            current_site = get_current_site(request)
            email_subject = 'Activate Your Account'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': force_text(urlsafe_base64_encode(force_bytes(user.pk))),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            return render(request, 'congratulation.html')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
    
def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, 'index.html')
    else:
        return HttpResponse('Activation link is invalid!')

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

class EditProfileView(UpdateView):
    model = User
    template_name = 'user-profile.html'
    form_class = UpdateProfileForm
    success_url = reverse_lazy('core:index-page')
    
    # def get_success_url(self):
    #     return reverse_lazy('accounts:user-profile', kwargs={'pk':self.get_object().pk})

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.username != self.get_object().username:
            raise PermissionDenied
        return super(EditProfileView, self).dispatch(request, *args, **kwargs)
