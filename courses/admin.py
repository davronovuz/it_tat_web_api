from django.contrib import admin
from .models import Course, Mentor, Portfolio, CourseLessonVideo, FeedbackMentor, Registration, FAQ, ProgramRequest, Technology

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'weekly_hours', 'duration_moths', 'total_hours', 'price_per_moths', 'discount', 'user_ai')
    search_fields = ('title',)

@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'experience_years', 'student_count')
    search_fields = ('first_name', 'last_name')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'mentor', 'url')
    search_fields = ('name', 'mentor__first_name', 'mentor__last_name')

@admin.register(CourseLessonVideo)
class CourseLessonVideoAdmin(admin.ModelAdmin):
    list_display = ('course', 'video')

@admin.register(FeedbackMentor)
class FeedbackMentorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'couse', 'mentor')

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'course')
    search_fields = ('first_name', 'last_name', 'phone_number')

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')

@admin.register(ProgramRequest)
class ProgramRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')
    search_fields = ('name', 'phone_number')

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    search_fields = ('title', 'course__title')



