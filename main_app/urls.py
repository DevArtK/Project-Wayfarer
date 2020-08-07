from django.urls import path, include
from . import views

urlpatterns = [
    # ----- Static / Public -----
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    # Auth Routes
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/signup", views.signup, name="signup"),
    # User Routes
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),
    path('users/<int:user_id>/edit/', views.user_edit, name='user_edit'),


    #Post Routes
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),

]
