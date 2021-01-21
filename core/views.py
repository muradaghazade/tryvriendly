from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from core.models import BetaUsers
from .forms import SignUpForBetaForm
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TermsView(TemplateView):
    template_name = 'termandconditions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UpcomingView(TemplateView):
    template_name = 'upcoming.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SuccessView(TemplateView):
    template_name = 'congratulation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SingUpForBetaView(CreateView):
    model = BetaUsers
    template_name = 'sign-for-beta.html'
    form_class = SignUpForBetaForm
    success_url = reverse_lazy('core:index-page')
