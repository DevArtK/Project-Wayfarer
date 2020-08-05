from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import User, Post, City

# from .forms import

# TEMP CAT DATA
class City: 
     def __init__(self, name, location):
       self.name = name
       self.location = location

City = [
     City('Atlanta', 'GA'),
     City('Norwalk', 'CT'),
     City('Brooklyn', 'NY'),
]

# ----- HOME Route -----
def home(request):
    return render(request, "home.html")


# ----- ABOUT Route -----
def about(request):
    return render(request, "about.html")


# ----- LOGIN Roue -----
def user_login(request):
    return render(request, "user/login.html")


# ----- SIGNUP Route -----
def user_signup(request):
    return render(request, "user/signup.html")


# ----- User Profile -----
def user_detail(request):
    # user: User.objects.get(id=user_id)
    # context - {"user": user}
    return render(request, "user/detail.html", {})


# ----- User Edit Profile, Posts -----
# TODO ---- Auth -----
def user_edit(request):
    return render(request, "user/edit.html")

