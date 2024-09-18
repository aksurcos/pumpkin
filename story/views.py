from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Story
from .forms import storyForm
import random
import os
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='accounts/login')
def story_create(request):  
    if request.method == 'POST':  
        form = storyForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.author = request.user
            story.save()
        
    else:
        form = storyForm()
    return render(request, "story_create.html", {
        "form": form
    })

def story(request):
    stories = Story.objects.all().order_by('-shared_at')
    return render (request, "story.html", {'stories': stories})

def story_details(request, slug):
    story = get_object_or_404(Story, slug=slug)
    context = {
        "story": story
    }
    return render(request, "story_details.html", context)



def MythList(request):
    return render (request, "myth.html")

def myth_details(request, id):
    return render(request, "myth-details.html",{"id":id})