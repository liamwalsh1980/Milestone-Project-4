from django.urls import path
from .import views

urlpatterns = [
    # Route URL
    path('', views.service_booking, name='service_booking'),
    path('add/<item_id>/', views.add_to_booking, name='add_to_booking'),
]