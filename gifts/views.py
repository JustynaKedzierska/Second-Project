from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Sum, Count, FloatField
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, FormView, ListView

from gifts.forms import LoginForm, AddUserForm
from gifts.models import Donation, Institution


class LandingPageViews(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(LandingPageViews, self).get_context_data(**kwargs)
        context['donation_count'] = Donation.objects.aggregate(sum_quantity=Sum('quantity'))
        context['institution_count'] = Donation.objects.aggregate(sum_institution=Count('institution', distinct=True)) # pobiera unikalne
        context['fundations'] = Institution.objects.filter(type='FUN')
        context['organizations'] = Institution.objects.filter(type='ORG')
        context['locals'] = Institution.objects.filter(type='LOK')
        return context


# class LoginView(TemplateView):
#     template_name = 'login.html'


class RegisterView(FormView):
    template_name = 'auth/register.html'
    model = User
    form_class = AddUserForm

    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)


class AddDonationView(TemplateView):
    template_name = 'form.html'


class LoginView(FormView):
    template_name = 'login.html'
    model = User
    form_class = LoginForm
    success_url = reverse_lazy('index')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')

