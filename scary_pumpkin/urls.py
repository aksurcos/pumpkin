from django.contrib import admin
from django.urls import path, include
from scary_pumpkin import views as index_views
from accounts import views as accounts_views
from story import views as story_views
from story import views as myth_views

urlpatterns = [
    path('', index_views.index, name='index'),   
    path('accounts/', accounts_views.accounts, name='accounts'),
    path('accounts/<int:id>', accounts_views.accounts_details, name='accounts_details'),
    path('story/', story_views.story, name='story'),
    path('story/<int:id>', story_views.story_details, name='story_details'),
    path('myth/', myth_views.myth, name='myth'),
    path('myth/<int:id>', myth_views.myth_details, name='myth_details'),
    path('admin/', admin.site.urls),
]