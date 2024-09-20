# Generated by Django 5.1.1 on 2024-09-20 18:04

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0005_story_edited_at_alter_comment_story'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
