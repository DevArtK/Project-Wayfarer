from django.urls import path
from . import views

urlpatterns = [
    # ----- Static / Public -----
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    # Auth Routes
    path("accounts/signup", views.signup, name="signup"),
<<<<<<< HEAD
    path("login/", views.login_user, name="login"),
]
=======
]
>>>>>>> 1fc2f17e8df9c8a45e9ba420973668c2afbdb9db
