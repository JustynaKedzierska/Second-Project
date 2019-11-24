from django.db.models import Sum, Count, FloatField
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from gifts.models import Donation


class LandingPageViews(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(LandingPageViews, self).get_context_data(**kwargs)
        context['donation_count'] = Donation.objects.aggregate(sum_quantity=Sum('quantity'))
        context['institution_count'] = Donation.objects.aggregate(sum_institution=Count('institution', distinct=True)) # pobiera unikalne
        return context


class LoginView(TemplateView):
    template_name = 'login.html'


class RegisterView(TemplateView):
    template_name = 'register.html'


class AddDonationView(TemplateView):
    template_name = 'form.html'
