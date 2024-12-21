from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'shoe', 'quantity', 'created_at')  
    list_filter = ('user', 'shoe', 'created_at')  
    search_fields = ('user__username', 'shoe__name')  
    ordering = ('-created_at',)  

    def get_queryset(self, request):
        """Расширение QuerySet для оптимизации запросов."""
        queryset = super().get_queryset(request)
        return queryset.select_related('user', 'shoe')
    