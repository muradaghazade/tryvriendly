from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView
from accounts.models import User, CreateIvent, GetRooms
from .forms import RegisterForm, LoginForm, ResetItDown, PasswordResetConfirmForm, UpdateProfileForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordChangeView
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.db import models

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, CreateEvent, UpdateUserSerializer, GetRoomSerializers
from django.utils.crypto import get_random_string
from knox.views import LoginView as KnoxLoginView

from knox.models import AuthToken
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
import random
import string

def usersignup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            if user.terms_agreement == True:
                user.save()
            else:
                raise PermissionDenied

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

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "status": "success",
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        #"token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format = None):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request,user)
        return super().post(request, format=None)


class CreateEventView(APIView):
    permission_classes=(permissions.IsAuthenticated,)

    def post(self, request):
        user = User.objects.get(email=request.user.email)
        if True:

            query = CreateIvent.objects.all()
            serializer = CreateEvent(query, many=True)

            return Response({"Status":"Room Created Successfully",
                             "Unique ID": ''.join(random.choice(string.digits) for _ in range(8))
})

        else:
            return Response({"Cannot Create Room"})

@api_view(['POST'])
def get_rooms(request):
    room=GetRooms.objects.all()
    if request.method=='GET':
        serializer=RoomSerializer(room,many=True)
        return Response(serializer.data)

    if request.method=='POST':
        serializer=GetRoomSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":request.data, "status":status.HTTP_201_CREATED})
        else:
            return Response(serializer.error,status=status.HTTP_404_NOT_FOUND)

class UpdateProfileView(generics.UpdateAPIView):

        if True:
            permission_classes = (permissions.IsAuthenticated,)
            queryset = User.objects.all()
            serializer_class = UpdateUserSerializer
            print(Response({"User Details Updated Successfulyy"}))
        else:
            print(Response({"User Details Does Not Updated"}))
