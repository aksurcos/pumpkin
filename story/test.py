from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Story, Comment
from .forms import storyForm, commentForm

class StoryFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        
        self.category1 = Category.objects.create(name='Test Category 1')
        self.category2 = Category.objects.create(name='Test Category 2')
        
        self.valid_form_data = {
            'title': 'Test Story',
            'country': 'Test Country',
            'categories': [self.category1.id, self.category2.id],
            'description': 'This is a test description.'
        }
        
        self.invalid_form_data = {
            'title': '',
            'country': 'Test Country',
            'categories': [],
            'description': 'This is a test description.'
        }

    def test_story_form_valid_data(self):
        form = storyForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid())

    def test_story_form_invalid_data(self):
        form = storyForm(data=self.invalid_form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertIn('categories', form.errors)

    def test_story_form_field_order(self):
        form = storyForm()
        self.assertEqual(list(form.fields.keys()), ['title', 'country', 'categories', 'description'])

class CommentFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        
        self.category = Category.objects.create(name='Test Category')
        self.story = Story.objects.create(
            title='Test Story',
            country='Test Country',
            description='Test Description',
            author=self.user
        )
        self.story.categories.add(self.category)
        
        self.valid_form_data = {
            'content': 'This is a test comment.'
        }
        
        self.invalid_form_data = {
            'content': ''
        }

    def test_comment_form_valid_data(self):
        form = commentForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid())

    def test_comment_form_invalid_data(self):
        form = commentForm(data=self.invalid_form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors)
        self.assertIn('Comment must not be empty.', form.errors['content'])