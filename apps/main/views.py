from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Shoes, Brend, Gender
from django.contrib import messages


class MainView(ListView):
    model = Shoes
    template_name = 'pages/home.html'
    context_object_name = 'shoes'
    

def home(request):
    shoes = Shoes.objects.all() 
    brand  = Brend.objects.all()
    print(f"Бренды: {list(brand)}")
    return render(request, 'pages/home.html', {'shoes': shoes, 'brand': brand})


def shoe_detail(request, pk):
    shoe = get_object_or_404(Shoes, pk=pk)  
    genders = Gender.objects.all()  
    
    return render(request, 'pages/shoe_detail.html', {
        'shoe': shoe,
        'genders': genders
    })

def order_success(request, shoe_id):
    shoe = get_object_or_404(Shoes, id=shoe_id)
    
    return render(request, 'pages/order_succes.html', {'shoe': shoe})

def order_shoe(request, pk):    
    if request.method == "POST":
        shoe = get_object_or_404(Shoes, pk=pk)
        quantity = int(request.POST.get('quantity', 1))
        
        messages.success(request, f'Вы успешно заказали {quantity} шт. {shoe.name}!')
        return redirect('order_succes', shoe_id=shoe.id)
    return redirect('home')




#def brands(request):
#    brends = Brend.objects.all()
#    return render(request, 'pages/home.html', {'brends': brends})




