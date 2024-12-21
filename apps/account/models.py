from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # Добавление дополнительных полей к модели пользователя, если нужно
    email = models.EmailField(unique=True)  # Поле email должно быть уникальным
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Номер телефона
    birth_date = models.DateField(null=True, blank=True)  # Дата рождения
    
    # Указание related_name для полей, чтобы избежать конфликта с группами и разрешениями
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Указываем имя обратной связи
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Указываем имя обратной связи
        blank=True
    )

    def __str__(self):
        return self.username  # Возвращаем username как строковое представление объекта
