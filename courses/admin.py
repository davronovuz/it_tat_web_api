from django.contrib import admin
from .models import Course, Portfolio, Mentor


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'weekly_hours', 'duration_moths', 'total_hours', 'price_per_moths',
                    'discount', 'user_ai', 'start_hour', 'description']  # 'description'ni list_display'ga qo'shdik
    list_filter = ['user_ai', 'start_hour']
    search_fields = ['title', 'description']
    list_display_links = ['title', 'description']  # Endi 'description' bu yerda ishlaydi


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description', 'mentor', 'url']
    list_filter = ['mentor']
    search_fields = ['name', 'description']
    list_display_links = ['name', 'image', 'description']


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'image', 'experience_years', 'student_count', 'description']  # 'courses'ni bu yerda olib tashladik
    list_filter = ['experience_years', 'student_count']
    search_fields = ['first_name', 'last_name', 'description']
    list_display_links = ['first_name', 'last_name', 'image', 'description']  # 'courses'ni olib tashladik, chunki bu Many-to-Many yoki FK
