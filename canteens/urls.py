from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import TemplateView


urlpatterns=[
	url(r'^$',views.restaurants),
	url(r'^gbnc/$',views.nc_gb),
	url(r'^3bnc/$',views.nc_3),
	url(r'^7bnc/$',views.nc_7),
	url(r'^8bnc/$',views.nc_8),
	url(r'^checkout/$',views.checkout),
	url(r'^checkout/bill$',views.bill)
	
]