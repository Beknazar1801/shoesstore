from django.db import models

# Create your models here.


class Gender(models.Model):
    CATEGORY_CHOICES = [
        ('M', 'Мужская'),
        ('Ж', 'Женская')
    ]
    name = models.CharField(max_length=1, choices=CATEGORY_CHOICES, unique=True, verbose_name="Категория пола")

    def __str__(self):
        return self.get_name_display()

class ShoeGenderAvailability(models.Model):
    shoe = models.ForeignKey('Shoes', on_delete=models.CASCADE, related_name='gender_availabilities')
    gender = models.ForeignKey('Gender', on_delete=models.CASCADE)  
    quantity = models.PositiveIntegerField(verbose_name="Доступное количество")

    def __str__(self):
        return f"{self.shoe.name} - {self.gender.get_name_display()} - {self.quantity} шт."

    class Meta:
        verbose_name = 'Доступность обуви по полу'
        verbose_name_plural = 'Доступности обуви по полу'


class Brend(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название бренда', unique=True)
    image = models.ImageField(upload_to='brend_images', verbose_name='Логотип бренда', null=True, blank=True)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name
    

class ShoeSize(models.Model):
    size = models.CharField(max_length=10, unique=True)  

    def __str__(self):
        return self.size


class Shoes(models.Model):
    name = models.CharField(max_length=60, verbose_name='Кроссовки')
    description = models.TextField('Описание обуви')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='shoes_images', null=True, blank=True)
    color = models.CharField(max_length=20, verbose_name='Цвет', null=True, blank=True)
    brend = models.ForeignKey('Brend', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Бренд')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')
    sizes = models.ManyToManyField(ShoeSize, related_name="shoes")
    gender = models.ForeignKey('ShoeGenderAvailability', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Пол')
    

    class Meta:
        verbose_name = 'Обувь'
        



    def total_available_quantity(self):
        return sum(availability.quantity for availability in self.shoesizeavailability_set.all())
    

    def __str__(self):
        return self.name
    
class ShoeSizeAvailability(models.Model):
    shoe = models.ForeignKey(Shoes, on_delete=models.CASCADE, verbose_name="Обувь")
    size = models.ForeignKey(ShoeSize, on_delete=models.CASCADE, verbose_name="Размер")
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, default=1)
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")  

    class Meta:
        unique_together = ('shoe', 'size')  
        verbose_name = "Наличие обуви"
        verbose_name_plural = "Наличие обуви"

    def __str__(self):
        return f"{self.shoe.name} - {self.size.size} - {self.quantity}"

    def is_available(self, requested_quantity):
        return self.quantity >= requested_quantity

    def reduce_quantity(self, requested_quantity):
        
        if self.is_available(requested_quantity):
            self.quantity -= requested_quantity
            self.save()
            return True
        return False
    


    
    

