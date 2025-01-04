from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Shoes, Brend, Gender,ShoeGenderAvailability, ShoeSizeAvailability
from django.contrib import messages


class MainView(ListView):
    model = Shoes
    template_name = 'pages/home.html'
    context_object_name = 'shoes'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brends'] = Brend.objects.all()
        return context
    

def home(request):
    shoes = Shoes.objects.all() 
    #brends = Brend.objects.all()
    return render(request, 'pages/home.html', {'shoes': shoes,}, )



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



def brands(request):
    brends = Brend.objects.all()
    return render(request, 'pages/brands.html', {'brends': brends})

def brand_detail(request, pk):
    brend = get_object_or_404(Brend, pk=pk)
    shoes = Shoes.objects.filter(brend=brend)
    return render(request, 'pages/brand_detail.html', {'brend': brend, 'shoes':shoes})


def mens_shoes(request):
    male_gender = Gender.objects.get(name='M')  # Мужская категория пола
    male_availabilities = ShoeGenderAvailability.objects.filter(gender=male_gender)

    # Получаем размеры для каждой обуви
    shoes_with_sizes = []
    for availability in male_availabilities:
        shoe = availability.shoe
        sizes = shoe.shoesizeavailability_set.all()
        shoes_with_sizes.append({'shoe': shoe, 'sizes': sizes})
    
    return render(request, 'pages/mens.html', {
        'male_availabilities': male_availabilities,
        'shoes_with_sizes': shoes_with_sizes
    })



def womens_shoes(request):
    female_gender = Gender.objects.get(name='Ж')  # Женская категория пола
    female_availabilities = ShoeGenderAvailability.objects.filter(gender=female_gender)

    # Получаем размеры для каждой обуви
    shoes_with_sizes = []
    for availability in female_availabilities:
        shoe = availability.shoe
        sizes = shoe.shoesizeavailability_set.all()
        shoes_with_sizes.append({'shoe': shoe, 'sizes': sizes})

    return render(request, 'pages/womens.html', {
        'female_availabilities': female_availabilities,
        'shoes_with_sizes': shoes_with_sizes
    })


def shoes_by_gender(request):
  
    male_gender = Gender.objects.get(name='M')
    female_gender = Gender.objects.get(name='Ж')

    
    male_availabilities = ShoeGenderAvailability.objects.filter(gender=male_gender).select_related('shoe', 'shoe__brend')
    female_availabilities = ShoeGenderAvailability.objects.filter(gender=female_gender).select_related('shoe', 'shoe__brend')

   
    return render(request, 'pages/shoes_by_gender.html', {
        'male_availabilities': male_availabilities,
        'female_availabilities': female_availabilities
    })

def shoe_search(request):
    query = request.GET.get('q', '').strip()
    results = []

    if query:
        results = Shoes.objects.filter(
            name__icontains=query  # Поиск по названию обуви
        ) | Shoes.objects.filter(
            brend__name__icontains=query  # Поиск по бренду (если поле brend связано с ForeignKey)
        )

    return render(request, 'pages/shoe_search.html', {'results': results, 'query': query})


  


