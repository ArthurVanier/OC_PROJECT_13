from django.urls import path
from django.contrib import admin
from .views import index, profile

urlpatterns = [
    path('', index, name='index'),
    path('profile/<str:username>/', profile, name='profile'),
]