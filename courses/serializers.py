from rest_framework import serializers
from .models import (
    Technology, Course, Portfolio, Mentor, CourseLessonVideo,
    FeedbackMentor, Registration, FAQ, ProgramRequest
)

class TechnologySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Technology
        fields = ['id', 'title', 'image', 'image_url', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def get_image_url(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image.url) if request else obj.image.url
        return None

class CourseSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True, read_only=True)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'description', 'duration_months', 'weekly_hours',
            'duration_hours', 'start_date', 'image', 'image_url', 'price_per_month',
            'discount', 'uses_ai', 'technologies','uzb_junior_salary','uzb_middle_salary','uzb_senior_salary','global_junior_salary','global_middle_salary','global_senior_salary','created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

    def get_image_url(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image.url) if request else obj.image.url
        return None

class PortfolioSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Portfolio
        fields = ['id', 'name', 'image', 'image_url', 'description', 'url', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def get_image_url(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image.url) if request else obj.image.url
        return None

class MentorSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    portfolios = PortfolioSerializer(many=True, read_only=True)
    image_url = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Mentor
        fields = [
            'id', 'first_name', 'last_name', 'full_name', 'image', 'image_url',
            'description', 'courses', 'experience_years', 'students_count',
            'portfolios', 'created_at', 'updated_at','projects_part_count','achievements_count'
        ]
        read_only_fields = ['created_at', 'updated_at']

    def get_image_url(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image.url) if request else obj.image.url
        return None

    def get_full_name(self, obj):
        return obj.get_full_name()

class CourseLessonVideoSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = CourseLessonVideo
        fields = ['id', 'title', 'course', 'video', 'video_url', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def get_video_url(self, obj):
        if obj.video and hasattr(obj.video, 'url'):
            request = self.context.get('request')
            return request.build_absolute_uri(obj.video.url) if request else obj.video.url
        return None

class FeedbackMentorSerializer(serializers.ModelSerializer):
    mentor = MentorSerializer(read_only=True)
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = FeedbackMentor
        fields = ['id', 'mentor', 'full_name', 'video', 'video_url', 'feedback_text', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def get_video_url(self, obj):
        if obj.video and hasattr(obj.video, 'url'):
            request = self.context.get('request')
            return request.build_absolute_uri(obj.video.url) if request else obj.video.url
        return None

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id', 'name', 'phone_number', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class ProgramRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramRequest
        fields = ['id', 'name', 'phone_number', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']