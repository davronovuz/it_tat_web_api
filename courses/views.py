from django.shortcuts import render
from .models import Course,Course_lesson_video,FeedbackMentor,Technology,FAQ,Registration,Mentor,Portfolio,ProgramRequest
from rest_framework import viewsets
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.prefetch_related("texnologiya").all()
    serializer_class = CourseSerializer

