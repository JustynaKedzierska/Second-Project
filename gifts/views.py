from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class LandingPageViews(TemplateView):
    template_name = 'index.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class RegisterView(TemplateView):
    template_name = 'register.html'


class AddDonationView(TemplateView):
    template_name = 'form.html'
