from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import Grade
from .forms import GradeForm

# Сторінка перегляду оцінок (Завдання 7)
@login_required
def grade_list(request):
    if request.user.is_superuser:
        # Адміністратор бачить всі оцінки
        grades = Grade.objects.all()
    else:
        # Звичайний користувач бачить тільки свої оцінки
        grades = Grade.objects.filter(student=request.user)
    
    # Сортування (Завдання 8)
    sort_by = request.GET.get('sort', '-date')
    allowed_sorts = ['date', '-date', 'subject', '-subject', 'grade', '-grade']
    if sort_by in allowed_sorts:
        grades = grades.order_by(sort_by)
    
    # Фільтрація (Завдання 9)
    subject_filter = request.GET.get('subject', '')
    if subject_filter:
        grades = grades.filter(subject=subject_filter)
    
    # Отримуємо всі предмети для фільтра
    subjects = Grade.objects.values_list('subject', flat=True).distinct()
    
    context = {
        'grades': grades,
        'subjects': subjects,
        'current_sort': sort_by,
        'current_subject': subject_filter,
    }
    return render(request, 'grades/grade_list.html', context)

# Додавання оцінки (Завдання 4)
@staff_member_required
def grade_create(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Оцінку успішно додано!')
            return redirect('grades:list')
    else:
        form = GradeForm()
    return render(request, 'grades/grade_form.html', {'form': form, 'title': 'Додати оцінку'})

# Редагування оцінки (Завдання 5)
@staff_member_required
def grade_update(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            messages.success(request, 'Оцінку успішно оновлено!')
            return redirect('grades:list')
    else:
        form = GradeForm(instance=grade)
    return render(request, 'grades/grade_form.html', {'form': form, 'title': 'Редагувати оцінку'})

# Видалення оцінки (Завдання 6)
@staff_member_required
def grade_delete(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == 'POST':
        grade.delete()
        messages.success(request, 'Оцінку успішно видалено!')
        return redirect('grades:list')
    return render(request, 'grades/grade_confirm_delete.html', {'grade': grade})