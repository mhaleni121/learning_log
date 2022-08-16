"""Defines URL patterns for users"""

from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


app_name = 'users'
urlpatterns = [
    # login
    path(r'^login/$', LoginView.as_view(template_name="registration/login.html"),  name='login'),
    # registering page
    path(r'register/', views.register, name='register'),
    # Logout page
    path(r'logout/', views.logout_view, name='logout'),

]

