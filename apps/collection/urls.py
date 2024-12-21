from django.contrib import admin
from django.urls import path, include
from .views import ShoesView

urlpatterns = [
    path('shoes/', ShoesView.as_view(), name='shoes'),
]
