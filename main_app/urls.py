from django.urls import path
from . import views

urlpatterns = [
    # ----- Static / Public -----
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    # Auth Routes
    path("accounts/signup", views.signup, name="signup"),
    path("login/", views.login_user, name="login"),
]
