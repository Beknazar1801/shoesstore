from .models import Brend
def all_brands(request):
    brends = Brend.objects.all()
    return {'brends': brends} 