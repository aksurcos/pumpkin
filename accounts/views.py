from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def accounts(request):
    return HttpResponse("This page will show the detail of accounts / users.")