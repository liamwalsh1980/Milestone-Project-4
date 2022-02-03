from django.urls import path
from .import views

urlpatterns = [
    # Route URL
    path('', views.index, name='home'),
    path('admin/', views.admin, name='admin')
]
