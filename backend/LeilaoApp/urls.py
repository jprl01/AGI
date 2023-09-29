from . import views
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView

router = routers.DefaultRouter()

urlpatterns = [
    path('clients/', views.getAllClients, name='getAllClients'),
    path('auction/',views.showAuctionProducts, name='showAuctionProducts'),
    # path('login/',views.login, name='login'),
    path('hello/',views.hello, name='hello'),
    path('createClient/',views.createClient,name='createClient'),
    path('auctionProduct/',views.auctionProduct, name='auctionProduct'),
    path('clientAuctionProducts/',views.showClientAuctionProducts, name='clientProducts'),
    path('showAuctionProducts/',views.showAuctionProducts, name='showAuctionProducts'),
    path('createAuctionProducts/',views.createAuctionProducts, name='createProducts'),
    path('closeAuctionProducts/',views.closeProductAuction, name='closeProducts'),
    # path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('addBalance/', views.addBalance, name='addBalance'),


    path("register/", RegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("user/", UserDetailsView.as_view(), name="rest_user_details"),
    

    
]
    
