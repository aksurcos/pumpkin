from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Story, Comment
# Register your models here.

@admin.register(Story)
class StoryAdmin(SummernoteModelAdmin):
    summernote_fields = ("description")
    list_display = ('title', 'description','country','shared_at')
    list_filter = ('author', 'country')
    search_fields = ('title', 'author', 'country')
    list_per_page = (10)
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    summernote_fields = ("content")
    list_display = ('author', 'created_at', 'story')
    list_filter = ('author', 'story')
    search_fields =('author', 'story')


