from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from apps.main.models import Shoes ,Shoes, ShoeSizeAvailability,Gender,ShoeGenderAvailability # Ваша модель Shoes
from .models import Order  # Модель заказа (если есть)
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def create_order(request, pk):
    shoe = get_object_or_404(Shoes, pk=pk)  

    if request.method == 'POST':
        size_id = int(request.POST.get('size')) 
        quantity = int(request.POST.get('quantity', 1))  
        gender_id = int(request.POST.get('gender')) 
        
        gender = get_object_or_404(Gender, id=gender_id)

        
        availability = ShoeSizeAvailability.objects.filter(
            shoe=shoe,
            size_id=size_id,
            gender=gender
        ).first()

        
        if not availability:
            messages.error(request, "Данный размер или пол недоступен для этой обуви.")
            return redirect('shoe_detail', pk=shoe.id)

        
        if quantity > availability.quantity:
            messages.error(request, "Недостаточно товара на складе.")
            return redirect('shoe_detail', pk=shoe.id)

        
        order = Order.objects.create(
            user=request.user,
            shoe=shoe,
            quantity=quantity,
            size_id=size_id,
            gender=gender 
        )

        
        availability.quantity -= quantity
        availability.save()

        
        messages.success(request, f'Вы успешно заказали {quantity} шт. {shoe.name} для пола {gender.name}!')
        return redirect('shoe_detail', pk=shoe.id)

    
    genders = Gender.objects.all()
    return render(request, 'pages/create_order.html', {'shoe': shoe, 'genders': genders})
