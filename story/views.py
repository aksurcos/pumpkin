from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def story(request):
    return render (request, "story.html")

def story_details(request, id):
    return render(request, "story-details.html", {"id":id})

def myth(request):
    return render (request, "myth.html")

def myth_details(request, id):
    return render(request, "myth-details.html",{"id":id})