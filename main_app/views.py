from django.shortcuts import render, HttpResponse, redirect

# from .models import
# from .forms import


# ----- HOME Route -----
def home(request):
    return render(request, "home.html")


# ----- ABOUT Route -----
def about(request):
    return render(request, "about.html")


# ----- LOGIN Roue -----
def login(request):
    return render(request, "login.html")


# ----- SIGNUP Route -----
def signup(request):
    return render(request, "signup.html")


# -----  -----


# -----  -----


# -----  -----
