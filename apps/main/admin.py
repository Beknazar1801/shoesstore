from django.contrib import admin
from .models import Brend, Shoes, ShoeSize,ShoeSizeAvailability, Gender, ShoeGenderAvailability

@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'brend', 'get_sizes')  # Используем метод get_sizes
    search_fields = ('name', 'brend')
    filter_horizontal = ('sizes',)  # Удобный виджет для управления многими ко многим

    def get_sizes(self, obj):
        """Вывод размеров в строку"""
        return ", ".join([size.size for size in obj.sizes.all()])
    get_sizes.short_description = 'Размеры'  # Подпись в админке


@admin.register(ShoeSize)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'size')
    search_fields = ('size',)


@admin.register(Brend)
class BrendAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')  # Поля для отображения в списке
    search_fields = ('name',)

@admin.register(ShoeSizeAvailability)
class ShoeSizeAvailabilityAdmin(admin.ModelAdmin):
    list_display = ('shoe', 'size', 'quantity')  # Отображаем обувь, размер и количество
    list_filter = ('shoe', 'size')
    search_fields = ('shoe__name', 'size__size') 

@admin.register(Gender)
class GenderCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(ShoeGenderAvailability)
class ShoeGenderAvailabilityAdmin(admin.ModelAdmin):
    list_display = ('shoe', 'gender', 'quantity')
    list_filter = ('gender', 'shoe')
    search_fields = ('shoe__name', 'gender__name')