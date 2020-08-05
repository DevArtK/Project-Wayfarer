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
def user_login(request):
    return render(request, "user/login.html")


# ----- SIGNUP Route -----
def user_signup(request):
    return render(request, "user/signup.html")


# -----  -----


# -----  -----

