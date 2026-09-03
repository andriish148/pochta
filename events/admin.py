from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_datetime', 'end_datetime', 'location', 'organizer', 'is_active')
    list_filter = ('start_datetime', 'location', 'is_active', 'organizer')
    search_fields = ('title', 'description', 'location')
    list_editable = ('is_active',)
    ordering = ('start_datetime',)
    
    fieldsets = (
        ('Основна інформація', {
            'fields': ('title', 'description', 'organizer')
        }),
        ('Дата та час', {
            'fields': ('start_datetime', 'end_datetime')
        }),
        ('Місце проведення', {
            'fields': ('location', 'online_link')
        }),
        ('Додатково', {
            'fields': ('image', 'is_active')
        }),
    )
    
    def has_add_permission(self, request):
        return request.user.is_superuser
    
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser
    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
    