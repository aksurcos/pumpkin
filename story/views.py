from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Story, Comment, Category
from .forms import storyForm, commentForm
from django.core.paginator import Paginator
import random
import os
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q, Count


#Create story

@login_required(login_url='accounts/login')
def story_create(request):  
    if request.method == 'POST':  
        form = storyForm(request.POST)

        if form.is_valid():
            story = form.save(commit=False)
            story.author = request.user          
            story.save()
            form.save_m2m()
            messages.success(request, "You have created story succesfully.")
            return redirect("story")
        
    else:
        form = storyForm()
    return render(request, "story_create.html", {
        "form": form
    })

#Posts List

def storyList(request):
    stories_list = Story.objects.all().order_by('-shared_at')
    paginator = Paginator(stories_list, 5)
    page_number = request.GET.get('page')
    stories = paginator.get_page(page_number)
    context = {
        'stories': stories
    }
    return render(request, "story.html", context)

#Filtered Posts

def story_list(request):
    stories = Story.objects.all().order_by('-shared_at')
    categories = Category.objects.all()
    
    selected_categories = request.GET.getlist('category')
    if selected_categories:
        stories = stories.filter(categories__name__in=selected_categories)\
                         .annotate(num_categories=Count('categories'))\
                         .filter(num_categories=len(selected_categories))\
                         .distinct()
    paginator = Paginator(stories, 5)
    page_number = request.GET.get('page')
    stories = paginator.get_page(page_number)
    
    context = {
        'stories': stories,
        'categories': categories,
        'selected_categories': selected_categories,
    }
    return render(request, "story.html", context)                    

def story_details(request, slug):
    story = get_object_or_404(Story, slug=slug)
    comments = Comment.objects.filter(story=story).order_by('-created_at')
    context = {
        "story": story,
        "comments": comments
    }
    return render(request, "story_details.html", context)

#Edit the post(by author)

@login_required
def edit(request, id):
    story = get_object_or_404(Story, id=id)
    if story.author != request.user:
        messages.error(request, "You don't have permission to edit this story.")
        return redirect('story_details', slug=story.slug)
    
    if request.method == 'POST':
        form = storyForm(request.POST, request.FILES, instance=story)
        if form.is_valid():
            story = form.save(commit=False)
            story.edited_at = timezone.now()
            story.save()
            form.save_m2m()
            messages.success(request, "Your story has been successfully updated!")
            return redirect('story_details', slug=story.slug)
        else:
            messages.error(request, "There was an error updating your story. Please check the form.")
    else: 
        form = storyForm(instance=story)
    
    context = {
        "form": form,
        "story": story
    }
    return render(request, "edit.html", context)
        
# Delete Post (by author)  
    
@login_required
def delete(request, id):
    story = get_object_or_404(Story, id=id)

    if story.author != request.user:
        context = {
        "story": story
    }
        return render(request, "story_details.html", context)
    
    if request.method == 'POST':
        messages.success(request, "Your story has been deleted successfully.")
        story.delete()
        return redirect('story')

    return render(request, "delete-confirm.html", {
        "story": story
    })

#Users to comment

@login_required
def add_comment(request, slug):
    story = get_object_or_404(Story, slug=slug)
    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.story = story
            comment.author = request.user
            comment.save()
            messages.success(request, "You've successfully commented.")
    return redirect ('story_details', slug=slug)
