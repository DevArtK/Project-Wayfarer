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
    # path('user/user_detail', views.user_detail, name='user_detail'),
    path('user/<int:user_id>', views.user_detail, name='user_profile'),
    path('user/edit/', views.user_edit, name='user_edit'),


    #Post Routes
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('post/new', views.post_add, name="post_add"),
    path('post/<int:post_id>/delete', views.post_delete, name='post_delete'),

    # City Routes
    path('city/index', views.city_index, name="city_index"),
    path('city/<int:city_id>/', views.city_detail, name="city_detail"),


]
