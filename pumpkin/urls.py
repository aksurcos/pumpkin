"""
URL configuration for pumpkin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from scary_pumpkin import views as index_views
from accounts import views as accounts_views
from story import views as story_views

urlpatterns = [
    path('', index_views.index, name='index'),   
    path('accounts/', accounts_views.accounts, name='accounts'),
    path('story/', story_views.story, name='story'),
    path('admin/', admin.site.urls),
]
