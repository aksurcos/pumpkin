from django import forms
from .models import Story
from django_summernote.widgets import SummernoteWidget

class storyForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = {'title','country', 'description'}
        labels = {
            'title' : 'Title of your story',
            'country' : 'Country',
            'desctription' : 'Details of your story'
        }

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'country' : forms.TextInput(attrs={'class':'form-control'}),
            'description': SummernoteWidget(attrs={'class':'form-control'}),           
                
        }

        error_messages = {
            'title' : {
                'min_length': "Title of story must be at least 4 characters.",
                'required' : "Title of story must not  be empty.",
            },

            'country' : {
                'required' : "You must write your country to understand local myths. "
            },

            'description' : {
                'required': "Description must not be empty"
            }
        }