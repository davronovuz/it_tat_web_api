from django.contrib import admin
from .models import Course, Mentor, Portfolio,Registration,Technology,Course_lesson_video,ProgramRequest,FeedbackMentor,FAQ


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

#
# @admin.register(Portfolio)
# class PortfolioAdmin(admin.ModelAdmin):
#     list_display = ('name', 'mentor', 'url')
#     list_filter = ('mentor',)
#     search_fields = ('name',)
#     ordering = ('name',)


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name','phone_number','course')
    list_filter = ('course',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)
    ordering = ('title',)


@admin.register(Course_lesson_video)
class Course_lesson_videoAdmin(admin.ModelAdmin):
    list_display = ('video','course')
    list_filter = ('course',)
    search_fields = ('course',)
    ordering = ('course',)

@admin.register(ProgramRequest)
class ProgramRequestAdmin(admin.ModelAdmin):
    list_display = ('name','phone_number')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(FeedbackMentor)
class FeedbackMentorAdmin(admin.ModelAdmin):
    list_display = ('full_name','mentor')
    list_filter = ('mentor',)
    search_fields = ('full_name','mentor','mentor')
    ordering = ('full_name',)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('title','description')
    list_filter = ('title','description')
    search_fields = ('title','description')
    ordering = ('title',)




