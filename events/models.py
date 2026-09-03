from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Event(models.Model):
    # Основна інформація
    title = models.CharField(
        max_length=200,
        verbose_name='Назва події'
    )
    description = models.TextField(
        verbose_name='Опис події'
    )
    
    # Дата та час
    start_datetime = models.DateTimeField(
        verbose_name='Дата та час початку'
    )
    end_datetime = models.DateTimeField(
        verbose_name='Дата та час закінчення'
    )
    
    # Місце проведення
    location = models.CharField(
        max_length=255,
        verbose_name='Місце проведення'
    )
    
    # Додаткові поля
    organizer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='organized_events',
        verbose_name='Організатор'
    )
    image = models.ImageField(
        upload_to='events/',
        blank=True,
        null=True,
        verbose_name='Фотографія'
    )
    online_link = models.URLField(
        blank=True,
        verbose_name='Посилання на онлайн-подію'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активна'
    )
    
    # Автоматичні поля
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата створення'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата оновлення'
    )
    
    class Meta:
        verbose_name = 'Подія'
        verbose_name_plural = 'Події'
        ordering = ['start_datetime']  # Сортування за датою
    
    def __str__(self):
        return self.title
    
    def is_past(self):
        """Перевірка, чи минула подія"""
        return timezone.now() > self.end_datetime
    
    def is_today(self):
        """Перевірка, чи подія сьогодні"""
        today = timezone.now().date()
        return self.start_datetime.date() <= today <= self.end_datetime.date()
    
    def is_future(self):
        """Перевірка, чи подія в майбутньому"""
        return timezone.now() < self.start_datetime