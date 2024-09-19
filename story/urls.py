from django.urls import path
from . import views

urlpatterns = [
    path('myth', views.MythList, name='myth'),
    path('myth/<int:id>', views.myth_details, name='myth_details'),
    path('story', views.storyList, name='story'),
    path('create', views.story_create, name='story_create'),
    path('delete/<int:id>', views.delete, name='delete_story'),
    path('story/<slug:slug>/', views.story_details, name='story_details'),
    
]