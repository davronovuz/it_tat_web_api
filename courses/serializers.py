from rest_framework import serializers
from .models import Course,Technology,Registration,FAQ,ProgramRequest,Mentor,\
    FeedbackMentor,Registration,FAQ,ProgramRequest,CourseLessonVideo,Portfolio



class TechnologySerializer(serializers.ModelSerializer):
    image=serializers.SerializerMethodField()

    class Meta:
        model = Technology
        fields = '__all__'

    def get_image(self,obj):
        request = self.context.get('request')
        image = obj.image.url
        return request.build_absolute_uri(image)


class CourseSerializer(serializers.ModelSerializer):
    image=serializers.SerializerMethodField()
    # technologies=serializers.TechnologySerializer(many=True,read_only=True)


    class Meta:
        model = Course
        fields = '__all__'

    def get_image(self,obj):
        request = self.context.get('request')
        image = obj.image.url
        return request.build_absolute_uri(image)

# class PortfolioSerializer(serializers.ModelSerializer):
#     image=serializers.SerializerMethodField()
#     class Meta:
#         model = Portfolio
#         fields = '__all__'
#
#     def get_image(self,obj):
#         request = self.context.get('request')
#         image = obj.image.url
#         return request.build_absolute_uri(image)
#
# class MentorSerializer(serializers.ModelSerializer):
#     image=serializers.SerializerMethodField()
#     portfolios=serializers.PortfolioSerializer(many=True,read_only=True)
#     courses=serializers.CourseSerializer(many=True,read_only=True)
#
#     class Meta:
#         model = Mentor
#         fields = '__all__'
#
#     def get_image(self,obj):
#         request = self.context.get('request')
#         image = obj.image.url
#         return request.build_absolute_uri(image)
#
#
#
# class RegistrationSerializer(serializers.ModelSerializer):
#     courses=serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
#     class Meta:
#         model = Registration
#         fields = '__all__'
#
#
# class FAQSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FAQ
#         fields = '__all__'
#
# class FeedbackMentorSerializer(serializers.ModelSerializer):
#     mentor = serializers.PrimaryKeyRelatedField(queryset=Mentor.objects.all())
#     video = serializers.SerializerMethodField()
#
#     class Meta:
#         model = FeedbackMentor
#         fields = '__all__'
#
#     def get_video(self,obj):
#         request = self.context.get('request')
#         video = obj.video.url
#         return request.build_absolute_uri(video)
#
#
#
# class CourseLessonVideoSerializer(serializers.ModelSerializer):
#     course=serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
#     video=serializers.SerializerMethodField()
#
#     class Meta:
#         model = CourseLessonVideo
#         fields = '__all__'
#
#
#     def get_video(self,obj):
#         request = self.context.get('request')
#         video = obj.video.url
#         return request.build_absolute_uri(video)
#
#
# class ProgramRequestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProgramRequest
#         fields = '__all__'
#
