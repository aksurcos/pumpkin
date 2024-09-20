from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_request, name='login'),
    path('register', views.register_request, name='register'),
    path('logout', views.logout_request, name='logout'),
    path('account/', views.account, name='account'),
    path('change_password', views.change_password, name='change_password'),
    
]