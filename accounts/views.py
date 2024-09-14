from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def accounts(request):
    return render (request, "accounts.html")

def accounts_details(request, id):
    return render(request, "accounts-details.html", {"id":id})