from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    # Route URL
    path('', views.index, name='home')
]
