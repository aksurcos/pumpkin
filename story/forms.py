from django import forms
from .models import Story, Comment, Category
from cloudinary.forms import CloudinaryFileField
from django_summernote.widgets import SummernoteWidget


class storyForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label='Categories',
    )

    class Meta:
        model = Story
        fields = {'title', 'country', 'categories', 'description', }
        labels = {
            'title': 'Give it a title',
            'country': 'Country',
            'categories': 'Categories',
            'description': 'Give details',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'on'}),
            'categories': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            }

        error_messages = {
            'title': {
                'min_length': "Title of story must be at least 4 characters.",
                'required': "Title of story must not  be empty.",
            },

            'country': {
                'required': "You must write your country to understand local myths. "
            },

            'description': {
                'required': "Description must not be empty"
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.order_fields(['title', 'country', 'categories', 'description'])


class commentForm (forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'content'}
        labels = {'content': 'Write your comment here.'}
        widgets = {'content': forms.Textarea(attrs={'class': 'form-control'})},
        error_messages = {
            'content': {'required': "Comment must not be empty."}}