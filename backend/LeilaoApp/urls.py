from . import views
from django.contrib import admin
from django.urls import path
from rest_framework import routers


router = routers.DefaultRouter()

urlpatterns = [
    path('clients/', views.getAllClients, name='getAllClients'),
]