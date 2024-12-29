from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, decorators

# Create your views here.

def home(request):
    return render(request, "index.html")

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    
    else:
        form = SignUpForm()
    
    return render(request, "signup.html", {"form": form})

@decorators.login_required(login_url="/login/")
def dashboard(request):
    return render(request, "dashboard.html", {'username': request.user.username})

@decorators.login_required(login_url="/login/")
def profile(request):
    return render(request, "profile.html", {
        'username': request.user.username,
        'email': request.user.email,
        'date_joined': request.user.date_joined,
        'last_login': request.user.last_login
    })
