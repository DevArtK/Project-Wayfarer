from django.urls import path
from . import views

urlpatterns = [
    # ----- Static / Public -----
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),

    path("user/detail", views.user_profile, name="user_details"),

    # Auth Routes
    path("accounts/signup", views.signup, name="signup"),
]
