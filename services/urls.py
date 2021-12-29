from django.urls import path
from .import views

urlpatterns = [
    # Route URL
    path('', views.all_services, name='services')
]
