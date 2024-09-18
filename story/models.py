from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.


class Story(models.Model):
    title = models.CharField(max_length=300)
    country = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    shared_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__ (self):
        return f"{self.title}, {self.country}, {self.author}"

    
    
