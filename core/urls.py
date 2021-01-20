from django.urls import path
from . import views

app_name = 'core'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index-page'),
    path('terms-and-conditions/', views.TermsView.as_view(), name='terms-page'),
    path('congratulation/', views.SuccessView.as_view(), name='congrats-page'),
    path('sing-up-for-beta/', views.SingUpForBetaView.as_view(), name='sing-for-beta-page'),
]
