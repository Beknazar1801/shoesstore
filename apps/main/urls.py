from .views import MainView
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('', views.home, name='home'),
    path('shoes/<int:pk>/', views.shoe_detail, name='shoe_detail'),
    path('order/<int:pk>/', views.order_shoe, name='order_shoe'),
    path('order_succes/<int:shoe_id>/', views.order_success, name='order_succes'),
    
]


