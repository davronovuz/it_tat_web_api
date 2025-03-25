from django.contrib import admin
from .models import Course, Mentor, Portfolio


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title','duration_months', 'weekly_hours', 'duration_hours', 'start_date', 'price_per_month')
    list_filter = ('duration_months', 'uses_ai')
    search_fields = ('title', 'description')
    ordering = ('title', 'description')


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'experience_years', 'students_count')
    list_filter = ('experience_years', 'students_count')
    search_fields = ('first_name', 'last_name')
    ordering = ('first_name', 'last_name')


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'mentor', 'url')
    list_filter = ('mentor',)
    search_fields = ('name',)
    ordering = ('name',)