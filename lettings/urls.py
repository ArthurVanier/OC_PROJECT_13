from django.urls import path
from django.contrib import admin
from .views import index, letting

urlpatterns = [
    path('', index, name='index'),
    path('letting/<int:letting_id>', letting, name="letting")
]