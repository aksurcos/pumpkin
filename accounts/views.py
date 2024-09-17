from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm
from accounts.forms import LoginUserForm, NewUserForm


# Create your views here.

def login_request(request):
    if request.user.is_authenticated:
        return redirect ("index")

    if request.method == "POST":
        print(form.is_valid())
        if form.is_valid():
            username =  form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, 'login.html', {'form':form})
    else:
        form = LoginUserForm()
        return render (request, 'login.html', {'form':form})           
    

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect("index")
        else:
            return render(request, "register.html")
    form = NewUserForm()
    return render(request, "register.html", {"form":form})

def logout_request(request):
    logout(request)
    messages.success(request, "You've been successfully logged out.")
    return redirect ("index")