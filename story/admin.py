from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Story, Comment, Category
# Register your models here.

@admin.register(Story)
class StoryAdmin(SummernoteModelAdmin):
    summernote_fields = ("description")
    list_display = ('title', 'author','country','shared_at', 'get_categories')
    list_filter = ('author', 'country', 'categories')
    search_fields = ('title', 'author', 'country')
    list_per_page = (10)
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all()])
    get_categories.short_description = 'Categories'

@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    summernote_fields = ("content")
    list_display = ('author', 'created_at', 'story')
    list_filter = ('author', 'story')
    search_fields =('author', 'story')

admin.site.register(Category)



