from django.contrib import admin
from .models import Course, Registration

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'instructor', 'duration', 'price', 'created_at']
    list_filter = ['instructor', 'created_at']
    search_fields = ['name', 'instructor']
    ordering = ['-created_at']

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'course', 'registration_date']
    list_filter = ['course', 'registration_date']
    search_fields = ['name', 'email', 'course__name']
    ordering = ['-registration_date']
    readonly_fields = ['registration_date']