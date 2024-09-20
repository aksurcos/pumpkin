from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone



# Create your models here.


class Story(models.Model):
    title = models.CharField(max_length=300)
    country = models.CharField(max_length=100)
    description = models.TextField(max_length=3000) 
    featured_image = CloudinaryField('image', default='placeholder')
    shared_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)
    edited_at = models.DateTimeField(null=True, blank=True)
    
        
    
    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__ (self):
        return f"{self.title}, {self.country}, {self.author}"

class Comment(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="comment")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}" commented on {self.story}'

    
    
