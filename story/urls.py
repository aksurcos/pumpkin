from django.urls import path
from . import views

urlpatterns = [
    path('', views.storyList, name='story'),
    path('filter/', views.story_list, name='story_list'),
    path('create/', views.story_create, name='story_create'),
    path('edit/<int:id>/', views.edit, name='edit_story'),
    path('delete/<int:id>/', views.delete, name='delete_story'),
    path('<slug:slug>/', views.story_details, name='story_details'),
    path('<slug:slug>/comment/', views.add_comment, name='add_comment'),
]