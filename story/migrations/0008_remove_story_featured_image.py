# Generated by Django 5.1.1 on 2024-09-22 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0007_category_story_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='featured_image',
        ),
    ]
