from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Story, Comment, Category
from .forms import storyForm, commentForm
from django.utils import timezone

class StoryCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Test Category')
        self.create_url = reverse('story_create')

    def test_story_create_GET(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'story_create.html')
        self.assertIsInstance(response.context['form'], storyForm)

    def test_story_create_POST_valid(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(self.create_url, {
            'title': 'Test Story',
            'country': 'Test Country',
            'categories': [self.category.id],
            'description': 'Test Description'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Story.objects.filter(title='Test Story').exists())

class StoryListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Test Category')
        self.story = Story.objects.create(
            title='Test Story',
            country='Test Country',
            description='Test Description',
            author=self.user
        )
        self.story.categories.add(self.category)
        self.list_url = reverse('story')

    def test_story_list_GET(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'story.html')
        self.assertIn('stories', response.context)

class StoryDetailsViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Test Category')
        self.story = Story.objects.create(
            title='Test Story',
            country='Test Country',
            description='Test Description',
            author=self.user,
            slug='test-story'
        )
        self.story.categories.add(self.category)
        self.details_url = reverse('story_details', args=[self.story.slug])

    def test_story_details_GET(self):
        response = self.client.get(self.details_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'story_details.html')
        self.assertIn('story', response.context)
        self.assertIn('comments', response.context)

class EditStoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Test Category')
        self.story = Story.objects.create(
            title='Test Story',
            country='Test Country',
            description='Test Description',
            author=self.user
        )
        self.story.categories.add(self.category)
        self.edit_url = reverse('edit_story', args=[self.story.id])

    def test_edit_story_GET(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.edit_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit.html')
        self.assertIsInstance(response.context['form'], storyForm)

    def test_edit_story_POST_valid(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(self.edit_url, {
            'title': 'Updated Test Story',
            'country': 'Updated Test Country',
            'categories': [self.category.id],
            'description': 'Updated Test Description'
        })
        self.assertEqual(response.status_code, 302)
        self.story.refresh_from_db()
        self.assertEqual(self.story.title, 'Updated Test Story')

class DeleteStoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Test Category')
        self.story = Story.objects.create(
            title='Test Story',
            country='Test Country',
            description='Test Description',
            author=self.user
        )
        self.story.categories.add(self.category)
        self.delete_url = reverse('delete_story', args=[self.story.id])

    def test_delete_story_POST(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Story.objects.filter(id=self.story.id).exists())

class AddCommentViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Test Category')
        self.story = Story.objects.create(
            title='Test Story',
            country='Test Country',
            description='Test Description',
            author=self.user,
            slug='test-story'
        )
        self.story.categories.add(self.category)
        self.add_comment_url = reverse('add_comment', args=[self.story.slug])

    def test_add_comment_POST_valid(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(self.add_comment_url, {'content': 'Test Comment'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Comment.objects.filter(content='Test Comment').exists())