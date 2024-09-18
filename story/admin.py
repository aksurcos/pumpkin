from django.contrib import admin
from .models import Story
# Register your models here.

class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','country','shared_at')
    list_filter = ('author', 'country')
    search_fields = ('title', 'author', 'country')
    list_per_page = (10)
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Story, StoryAdmin)
