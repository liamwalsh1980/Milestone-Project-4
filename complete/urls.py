from django.urls import path
from .import views

urlpatterns = [
    path('', views.complete, name='complete'),
    path('booking_success/<booking_number>',
         views.booking_success, name='booking_success'),
]
