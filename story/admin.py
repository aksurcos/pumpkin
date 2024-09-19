from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Story
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


