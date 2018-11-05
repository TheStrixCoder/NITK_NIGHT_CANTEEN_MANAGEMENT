from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import TemplateView


urlpatterns=[
	url(r'^$',views.home),
	url('^login/$',views.login),
	url('^logout/$',views.logout),
	url(r'^register/$',views.register_user),
]