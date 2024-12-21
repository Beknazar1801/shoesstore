from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView


# Create your views here.

class ShoesView(TemplateView):
    template_name = 'pages/shoes.html'
    


