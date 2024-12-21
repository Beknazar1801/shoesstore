from django.db import models
from django.contrib.auth.models import User
from apps.main.models import Shoes, Gender,ShoeSize

class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Пользователь', null=True, blank=True)
    shoe = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    size = models.ForeignKey(ShoeSize, on_delete=models.CASCADE, null=True, blank=True)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Заказ {self.user.username} - {self.shoe.name} ({self.quantity} шт.)"
