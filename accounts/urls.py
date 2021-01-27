from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from . import views
from accounts.views import LoginUserView, ResetPassword, CustomPasswordResetConfirmView, EditProfileView

app_name = 'accounts'

urlpatterns = [
    path('register/', views.usersignup, name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('user-profile/<slug:slug>', EditProfileView.as_view(), name='user-profile'),
    path('log-out', LogoutView.as_view(), name='log-out'),
    path('reset-password', ResetPassword.as_view(), name='reset-password'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate_account, name='activate'),
    # path('change-password', ThePasswordChangeView.as_view(), name='change-password'),
    # path('edit-profile/<int:pk>/', EditProfileView.as_view(), name='edit_profile'),
    path('password-reset-confirm/<str:uidb64>/<str:token>/', CustomPasswordResetConfirmView.as_view(), name = 'password-reset-confirm'),
    path('register-api/', views.RegisterAPI.as_view(), name='registerApi'),
    path('login-api/', views.LoginAPI.as_view(), name='loginApi'),
    path('create-rooms/', views.CreateEvent.as_view(), name='createroom')
]
