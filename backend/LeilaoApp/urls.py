from . import views
from django.contrib import admin
from django.urls import path
from rest_framework import routers


router = routers.DefaultRouter()

urlpatterns = [
    path('clients/', views.getAllClients, name='getAllClients'),
    path('auction/',views.showAuctionProducts, name='showAuctionProducts'),
    path('login/',views.login, name='login'),
    path('hello/',views.hello, name='hello'),
    path('createClient/',views.createClient,name='createClient'),
    path('auctionProduct/',views.auctionProduct, name='auctionProduct'),
    path('clientAuctionProducts/',views.showClientAuctionProducts, name='clientProducts'),
    path('showAuctionProducts/',views.showAuctionProducts, name='showAuctionProducts'),
    path('createAuctionProducts/',views.createAuctionProducts, name='createProducts'),
    path('closeAuctionProducts/',views.closeProductAuction, name='closeProducts'),

    
]
    
