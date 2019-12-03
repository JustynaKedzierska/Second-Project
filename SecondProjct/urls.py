"""SecondProjct URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static


from gifts.views import LandingPageViews, LoginView, RegisterView, AddDonationView, LogoutView, UserDetail, \
    AddDonationConfirmationView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', LandingPageViews.as_view(), name='index'),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^register/', RegisterView.as_view(), name='register'),
    url(r'^donation-add/', AddDonationView.as_view(), name='donation-add'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^user/detail/(?P<pk>(\d)+)', UserDetail.as_view(), name="user-detail"),
    url(r'^donation-confirmation/', AddDonationConfirmationView.as_view(), name='donation-confirmation'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
