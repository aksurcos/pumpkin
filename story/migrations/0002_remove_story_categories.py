# Generated by Django 5.1.1 on 2024-09-18 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='categories',
        ),
    ]
