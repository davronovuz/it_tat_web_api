from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from .models import (
    Technology, Course, Portfolio, Mentor, CourseLessonVideo,
    FeedbackMentor, Registration, FAQ, ProgramRequest
)
from .serializers import (
    TechnologySerializer, CourseSerializer, PortfolioSerializer,
    MentorSerializer, CourseLessonVideoSerializer, FeedbackMentorSerializer,
    RegistrationSerializer, FAQSerializer, ProgramRequestSerializer
)




class HomeAPIView(APIView):
    def get(self, request, format=None):
        # Faqat ReDoc va Swagger linklari
        endpoints = {
            "swagger": reverse("schema-swagger-ui", request=request),
            "redoc": reverse("schema-redoc", request=request),
        }
        return Response({
            "message": "IT TAT web sayti API dokumentatsiya sahifasi",
            "endpoints": endpoints
        })






# Technology ViewSet
class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    # Bu yerda prefetch_related kerak emas, chunki aloqalar yo‘q

# Course ViewSet
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.prefetch_related('technologies')
    serializer_class = CourseSerializer
    # 'technologies' ManyToManyField uchun prefetch_related ishlatildi

# Portfolio ViewSet
class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    # Bu yerda prefetch_related kerak emas, chunki aloqalar yo‘q

# Mentor ViewSet
class MentorViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.prefetch_related('courses', 'portfolios')
    serializer_class = MentorSerializer
    # 'courses' va 'portfolios' ManyToManyField uchun prefetch_related ishlatildi

# CourseLessonVideo ViewSet
class CourseLessonVideoViewSet(viewsets.ModelViewSet):
    queryset = CourseLessonVideo.objects.select_related('course')
    serializer_class = CourseLessonVideoSerializer
    # 'course' ForeignKey uchun select_related ishlatildi

# FeedbackMentor ViewSet
class FeedbackMentorViewSet(viewsets.ModelViewSet):
    queryset = FeedbackMentor.objects.select_related('mentor')
    serializer_class = FeedbackMentorSerializer
    # 'mentor' ForeignKey uchun select_related ishlatildi

# Registration ViewSet
class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.select_related('course')
    serializer_class = RegistrationSerializer
    # 'course' ForeignKey uchun select_related ishlatildi

# FAQ ViewSet
class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    # Bu yerda prefetch_related kerak emas, chunki aloqalar yo‘q

# ProgramRequest ViewSet
class ProgramRequestViewSet(viewsets.ModelViewSet):
    queryset = ProgramRequest.objects.all()
    serializer_class = ProgramRequestSerializer
    # Bu yerda prefetch_related kerak emas, chunki aloqalar yo‘q