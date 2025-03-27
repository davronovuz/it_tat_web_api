from django.contrib import admin
from .models import Course, Mentor, Portfolio, Technology, CourseLessonVideo, FeedbackMentor, Registration,FAQ,ProgramRequest


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


# @admin.register(Portfolio)
# class PortfolioAdmin(admin.ModelAdmin):
#     list_display = ('name', 'mentor', 'url')
#     list_filter = ('mentor',)
#     search_fields = ('name',)
#     ordering = ('name',)


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_filter = ('title',)
    search_fields = ('title',)
    ordering = ('title',)


@admin.register(FeedbackMentor)
class FeedbackMentorAdmin(admin.ModelAdmin):
    list_display = ('mentor', 'full_name', 'video', 'feedback_text')
    list_filter = ('mentor',)
    search_fields = ('full_name',)
    ordering = ('full_name',)



@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'course')
    list_filter = ('course',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(CourseLessonVideo)
class CourseLessonVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'video')
    list_filter = ('course',)
    search_fields = ('title',)
    ordering = ('title',)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    list_filter = ('question',)
    search_fields = ('question',)
    ordering = ('question',)



@admin.register(ProgramRequest)
class ProgramRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)







