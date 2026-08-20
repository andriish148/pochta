from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='profile',
        verbose_name='Користувач'
    )
    avatar = models.ImageField(
        upload_to='avatars/', 
        blank=True, 
        null=True,
        verbose_name='Фото профілю'
    )
    bio = models.TextField(
        blank=True,
        verbose_name='Про себе'
    )
    birth_date = models.DateField(
        blank=True, 
        null=True,
        verbose_name='Дата народження'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата створення'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата оновлення'
    )
    
    class Meta:
        verbose_name = 'Профіль'
        verbose_name_plural = 'Профілі'
        ordering = ['user__username']
    
    def __str__(self):
        return f'Профіль користувача {self.user.username}'