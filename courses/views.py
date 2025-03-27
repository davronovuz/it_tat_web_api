from django.shortcuts import render
from .models import Course, Portfolio, Mentor, Technology, \
    CourseLessonVideo, FeedbackMentor, Registration, FAQ, ProgramRequest

from .serializers import CourseSerializer

from rest_framework import viewsets


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.prefetch_related('technologies').all()
    serializer_class = CourseSerializer






