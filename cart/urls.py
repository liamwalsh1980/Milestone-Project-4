from django.urls import path
from .import views

urlpatterns = [
    # Route URL
    path('', views.view_cart, name='view_cart')
]
