from django.contrib import admin
from .models import FeedbackMentor, Mentor, Portfolio, ProgramRequest, Registration, Technology, Course, FAQ, CourseLessonVideo


@admin.register(FeedbackMentor)
class FeedbackMentorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'mentor', 'video')
    search_fields = ('full_name', 'mentor__first_name', 'mentor__last_name')
    list_filter = ('mentor',)

@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'experience_years', 'student_count')
    search_fields = ('first_name', 'last_name')
    list_filter = ('experience_years',)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'url')
    search_fields = ('name',)

@admin.register(ProgramRequest)
class ProgramRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')
    search_fields = ('name', 'phone_number')

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'course')
    search_fields = ('first_name', 'last_name', 'phone_number', 'course__title')
    list_filter = ('course',)

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'weekly_hours', 'duration_moths', 'total_hours', 'price_per_moths')
    search_fields = ('title',)
    list_filter = ('duration_moths', 'weekly_hours')

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('title', 'question', 'answer')
    search_fields = ('title', 'question')

@admin.register(CourseLessonVideo)
class CourseLessonVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'video')
    search_fields = ('title', 'course__title')
