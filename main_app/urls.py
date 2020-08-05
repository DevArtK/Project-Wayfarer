from django.urls import path
from . import views

urlpatterns = [
    # ----- Static / Public -----
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("login/", views.user_login, name="login"),
    path("signup/", views.user_signup, name="signup"),
    # ----- User profile-----
    path("user/", views.user_detail, name="detail"),
    path("user/edit", views.user_edit, name="edit"),
]
