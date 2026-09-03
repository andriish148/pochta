from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Event
from .forms import EventForm

# Сторінка списку подій (Завдання 7)
class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # Фільтрація за статусом
        status = self.request.GET.get('status', 'all')
        now = timezone.now()
        
        if status == 'future':
            queryset = queryset.filter(start_datetime__gt=now)
        elif status == 'past':
            queryset = queryset.filter(end_datetime__lt=now)
        elif status == 'today':
            today = now.date()
            queryset = queryset.filter(
                start_datetime__date__lte=today,
                end_datetime__date__gte=today
            )
        
        return queryset.order_by('start_datetime')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

# Детальна сторінка події (Завдання 9)
class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'

# Створення події (Завдання 4)
class EventCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('events:list')
    
    def test_func(self):
        return self.request.user.is_superuser
    
    def form_valid(self, form):
        form.instance.organizer = self.request.user
        messages.success(self.request, 'Подію успішно створено!')
        return super().form_valid(form)

# Редагування події (Завдання 5)
class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('events:list')
    
    def test_func(self):
        return self.request.user.is_superuser
    
    def form_valid(self, form):
        messages.success(self.request, 'Подію успішно оновлено!')
        return super().form_valid(form)

# Видалення події (Завдання 6)
class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('events:list')
    
    def test_func(self):
        return self.request.user.is_superuser
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Подію успішно видалено!')
        return super().delete(request, *args, **kwargs)