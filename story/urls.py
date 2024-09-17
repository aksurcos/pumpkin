from django.urls import path
from . import views

urlpatterns = [
    path('myth', views.myth, name='myth'),
    path('myth_details/<int:id>', views.myth_details, name='myth_details'),
    path('story', views.story, name='story'),
    path('story_details/<int:id>', views.story_details, name='story_details'),

]