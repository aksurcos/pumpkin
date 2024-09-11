from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def story(request):
    return HttpResponse("On this page, stories will be posted.")