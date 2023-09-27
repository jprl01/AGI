from . import views
from django.contrib import admin
from django.urls import path
from rest_framework import routers


router = routers.DefaultRouter()

urlpatterns = [
    path('clients/', views.getAllClients, name='getAllClients'),
    path('auction/',views.showAuctionProducts, name='showAuctionProducts'),
    path('login',views.login, name='login'),
    path('hello',views.hello, name='hello'),

    
]