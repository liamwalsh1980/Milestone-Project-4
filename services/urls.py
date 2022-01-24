from django.urls import path
from .import views

urlpatterns = [
    # Route URL
    path('', views.all_services, name='services'),
    path('<int:service_id>/', views.service_detail, name='service_detail'),
    # path('book/', views.service_booking, name='service_booking'),
]
