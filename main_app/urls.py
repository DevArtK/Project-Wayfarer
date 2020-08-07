from django.urls import path, include
from . import views

urlpatterns = [
    # ----- Static / Public -----
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),

    path("user/detail", views.user_profile, name="user_details"),

    # Auth Routes
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/signup", views.signup, name="signup"),
    # User Routes
    path('user/<int:user_id>/', views.user_detail, name='detail'),
    path('post/', views.post_index, name='post')
]
