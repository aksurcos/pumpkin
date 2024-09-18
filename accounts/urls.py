from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_request, name='login'),
    path('register', views.register_request, name='register'),
    path('logout', views.logout_request, name='logout'),
    path('account_details', views.account_details, name='account_details'),
    path('change_password', views.change_password, name='change_password')
]