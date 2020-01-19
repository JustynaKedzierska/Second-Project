from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.db.models import Sum, Count, FloatField
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, FormView, ListView, DetailView

from gifts.forms import LoginForm, AddUserForm, AddDonationForm
from gifts.models import Donation, Institution, Category


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


class AddDonationView(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    model = Donation
    fields = ['quantity', 'categories', 'institution', 'address', 'phone_number', 'city', 'zip_code', 'pick_up_date',
              'pick_up_time', 'pick_up_comment', 'user']
    # widgets = {
    #     'categories': forms.CheckboxSelectMultiple()
    # }
    success_url = reverse_lazy('index')
    login_url = '/login/'


    def get_context_data(self, **kwargs):
        context = super(AddDonationView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['institutions'] = Institution.objects.all()
        return context


class AddDonationConfirmationView(TemplateView):
    template_name = 'form-confirmation.html'


class LoginView(FormView):
    template_name = 'login.html'
    model = User
    form_class = LoginForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = User.objects.get(email=form.cleaned_data['email'])
        if user is not None:
            user = authenticate(username=user.username,
                                password=form.cleaned_data['password'])
            if user is not None:
                login(self.request, user)

            return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        user = form.cleaned_data['email']
        if user is not None:
            return reverse_lazy('register')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class UserDetail(LoginRequiredMixin, DetailView):
    model = User

