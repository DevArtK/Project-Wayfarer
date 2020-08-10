from django.urls import path, include
from . import views

urlpatterns = [
    # ----- Static / Public -----
    path("", views.home, name="home"),
    path("city/", views.city, name="city"),    
    # ---- Cities ---------
    path("au/", views.au, name="au"),
    path("boston/", views.boston, name="boston"),
    path("charlotte/", views.charlotte, name="charlotte"),
    path("columbus/", views.columbus, name="columbus"),
    path("denver/", views.denver, name="denver"),
    path("detroit/", views.detroit, name="detroit"),
    path("elpaso/", views.elpaso, name="elpaso"),
    path("fortworth/", views.fortworth, name="fortworth"),
    path("indianapolis/", views.indianapolis, name="indianapolis"),
    path("jacksonville/", views.jacksonville, name="jacksonville"),
    path("lasvegas/", views.lasvegas, name="lasvegas"),
    path("louisville/", views.louisville, name="louisville"),
    path("memphis/", views.memphis, name="memphis"),
    path("milwaukee/", views.milwaukee, name="milwaukee"),
    path("nashville/", views.nashville, name="nashville"),
    path("oklahoma/", views.oklahoma, name="oklahoma"),
    path("portland/", views.portland, name="portland"),
    path("sanfrancisco/", views.sanfrancisco, name="sanfrancisco"),
    path("seattle/", views.seattle, name="seattle"),
    path("washington/", views.washington, name="washington"),
    path("albuquerque/", views.albuquerque, name="albuquerque"),
    path("tucson/", views.tucson, name="tucson"),
    path("fresno/", views.fresno, name="fresno"),
    path("sacremento/", views.sacremento, name="sacremento"),
    path("mesa/", views.mesa, name="mesa"),
    path("bal/", views.bal, name="bal"),




    


    path("user/detail", views.user_profile, name="user_details"),

    # Auth Routes
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/signup", views.signup, name="signup"),
    # User Routes
    path('user/<int:user_id>/', views.user_detail, name='detail'),
    path('post/', views.post_index, name='post')
]
