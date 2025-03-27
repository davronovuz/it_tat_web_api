from rest_framework import serializers
from .models import Course,Course_lesson_video,FeedbackMentor,Technology,FAQ,Registration,Mentor,Portfolio,ProgramRequest


class TechnologySerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Technology
        fields = "__all__"

    def get_images(self, obj):
        requests = self.context.get('request')
        image = obj.image.url
        return requests.build_absolute_uri(image)

class CourseSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    technologies = serializers.TechnologySerializer(many=True, read_only=True)
    mentors = serializers.MentorSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"

    def get_images(self, obj):
        requests = self.context.get('request')
        image = obj.image.url
        return requests.build_absolute_uri(image)



class PortfolioSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Portfolio
        fields = "__all__"

    def get_images(self, obj):
        requests = self.context.get('request')
        image = obj.image.url
        return requests.build_absolute_uri(image)


class MentorSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    portfolio = serializers.PortfolioSerializer(many=True, read_only=True)
    courses = serializers.CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Mentor
        fields = "__all__"

    def get_images(self, obj):
        requests = self.context.get('request')
        image = obj.image.url
        return requests.build_absolute_uri(image)

class RegistrationSerializers(serializers.ModelSerializer):
    courses=serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())

    class Meta:
        model=Registration
        fields="__all__"

class FeedbackMentorSerializers(serializers.ModelSerializer):
    mentor=serializers.PrimaryKeyRelatedField(queryset=Mentor.objects.all())
    video=serializers.SerializerMethodField()

    class Meta:
        model=FeedbackMentor
        fields="__all__"

    def get_video(self, obj):
        requests = self.context.get('request')
        video = obj.image.url
        return requests.build_absolute_uri(video)

class Course_lesson_videoSerializer(serializers.ModelSerializer):
    course=serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    video=serializers.SerializerMethodField()
    class Meta:
        model=Course_lesson_video
        fields="__all__"

    def get_video(self, obj):
        requests = self.context.get('request')
        video = obj.image.url
        return requests.build_absolute_uri(video)


class ProgramRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProgramRequest
        fields="__all__"

