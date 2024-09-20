from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone



# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Story(models.Model):
    title = models.CharField(max_length=300)
    categories = models.ManyToManyField(Category)
    country = models.CharField(max_length=100)
    description = models.TextField(max_length=3000) 
    featured_image = CloudinaryField('image', default='placeholder')
    shared_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)
    edited_at = models.DateTimeField(null=True, blank=True)  
         
    def save(self, *args, **kwargs):
        if not self.slug or self.title != Story.objects.get(id=self.id).title:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def generate_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Story.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

class Comment(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="comment")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}" commented on {self.story}'

    
    
