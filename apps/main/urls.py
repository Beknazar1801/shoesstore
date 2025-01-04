from .views import MainView
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('shoes/', views.home, name='shoes'),
    path('brands/', views.brands, name='brands'),
    path('shoes/<int:pk>/', views.shoe_detail, name='shoe_detail'),
    path('order/<int:pk>/', views.order_shoe, name='order_shoe'),
    path('order_succes/<int:shoe_id>/', views.order_success, name='order_succes'),
    path('brands/<int:pk>/', views.brand_detail, name='brand_detail'),
    path('mens-shoes/', views.mens_shoes, name='mens'),
    path('womens-shoes/', views.womens_shoes, name='womens'),
    path('shoes-by-gender/', views.shoes_by_gender, name='shoes_by_gender'),
    path('search/', views.shoe_search, name='shoe_search'),
    
]


