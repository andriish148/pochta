from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Grade(models.Model):
    student = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='grades',
        verbose_name='Учень'
    )
    subject = models.CharField(
        max_length=100,
        verbose_name='Предмет/дисципліна'
    )
    grade = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)],
        verbose_name='Оцінка'
    )
    date = models.DateField(
        verbose_name='Дата отримання'
    )
    work_name = models.CharField(
        max_length=200,
        verbose_name='Назва роботи'
    )
    comment = models.TextField(
        blank=True,
        verbose_name='Коментар викладача'
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
        verbose_name = 'Оцінка'
        verbose_name_plural = 'Оцінки'
        ordering = ['-date']  # Нові оцінки першими
    
    def __str__(self):
        return f'{self.student.username} - {self.subject}: {self.grade}'