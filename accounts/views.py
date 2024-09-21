from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm
from accounts.forms import LoginUserForm, NewUserForm
from story.models import Story
from django.contrib.auth.decorators import login_required


#Login

def login_request(request):
    if request.user.is_authenticated:
        return redirect ("index")

    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username =  form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
    
            if user is not None:
                login(request, user)
                messages.success(request, "Welcome, you have logged in successfully.")
                return redirect("index")            
            else:
                return render(request, 'login.html', {'form':form})                
        else:
            messages.warning(request, "You could not log in.")
            return render(request, 'login.html', {'form':form})
    else:
        form = LoginUserForm()
        return render (request, 'login.html', {'form':form})           
    
#Register

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, "Welcome, You have successfully registered.")
            return redirect("index")
        else:
            return render(request, "register.html", {"form":form})
    form = NewUserForm()
    return render(request, "register.html", {"form":form})

#Logout

def logout_request(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect ("index")

#Change Password

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password has been changed")
            return redirect("account_details")
        else:
            messages.warning(request, "Your password has not been changed. Check again")
            return render(request, "change-password.html", {"form":form})
    
    form = PasswordChangeForm(request.user)
    return render(request, "change-password.html", {"form":form})

#Display own profile page

@login_required
def account(request):
    user_stories = Story.objects.filter(author=request.user).order_by('-shared_at')
    context = {
        'user_stories': user_stories
    }
    return render(request, 'account.html', context)