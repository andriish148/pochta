from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('home')

def register(request):
    """
    Сторінка реєстрації нового користувача
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Зберігаємо користувача
            user = form.save()
            
            # Автоматично входимо після реєстрації
            login(request, user)
            
            # Повідомлення про успіх
            messages.success(request, f'Вітаємо, {user.username}! Ви успішно зареєструвалися!')
            
            # Перенаправляємо на головну сторінку
            return redirect('home')
        else:
            # Якщо форма невалідна - показуємо помилки
            messages.error(request, 'Будь ласка, виправте помилки у формі.')
    else:
        form = RegisterForm()
    
    return render(request, 'users/register.html', {'form': form})

# Create your views here.
