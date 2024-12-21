from django.urls import path
from . import views

urlpatterns = [
    path('order_create/<int:pk>/', views.create_order, name='create_order'),
    
    
    
    
]
