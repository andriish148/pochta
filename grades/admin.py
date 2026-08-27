from django.contrib import admin
from .models import Grade

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'grade', 'date', 'work_name')
    list_filter = ('subject', 'date', 'student')
    search_fields = ('student__username', 'student__email', 'subject', 'work_name')
    list_editable = ('grade',)
    ordering = ('-date',)
    
    fieldsets = (
        ('Основна інформація', {
            'fields': ('student', 'subject', 'grade', 'date')
        }),
        ('Деталі', {
            'fields': ('work_name', 'comment')
        }),
    )
    
    # Обмежуємо доступ: тільки адміністратор може додавати/змінювати/видаляти
    def has_add_permission(self, request):
        return request.user.is_superuser
    
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser
    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser