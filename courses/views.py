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
    MentorSerializer, CourseVideoSerializer, FeedbackSerializer,
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



# Course ViewSet
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.prefetch_related('technologies')
    serializer_class = CourseSerializer

# Portfolio ViewSet
class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


# Mentor ViewSet
class MentorViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.prefetch_related('courses', 'portfolios')
    serializer_class = MentorSerializer

# CourseLessonVideo ViewSet
class CourseLessonVideoViewSet(viewsets.ModelViewSet):
    queryset = CourseLessonVideo.objects.select_related('course')
    serializer_class = CourseVideoSerializer


# FeedbackMentor ViewSet
class FeedbackMentorViewSet(viewsets.ModelViewSet):
    queryset = FeedbackMentor.objects.select_related('mentor')
    serializer_class = FeedbackSerializer


# Registration ViewSet
class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.select_related('course')
    serializer_class = RegistrationSerializer


# FAQ ViewSet
class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


# ProgramRequest ViewSet
class ProgramRequestViewSet(viewsets.ModelViewSet):
    queryset = ProgramRequest.objects.all()
    serializer_class = ProgramRequestSerializer
