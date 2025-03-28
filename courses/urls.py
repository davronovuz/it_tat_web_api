from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, MentorViewSet, PortfolioViewSet, CourseLessonVideoViewSet,FeedbackMentorViewSet, RegistrationViewSet, FAQViewSet, ProgramRequestViewSet, TechnologyViewSet


drouter = DefaultRouter()
drouter.register(r'courses', CourseViewSet)
drouter.register(r'mentors', MentorViewSet)
drouter.register(r'portfolios', PortfolioViewSet)
drouter.register(r'course-videos', CourseLessonVideoViewSet)
drouter.register(r'feedbacks', FeedbackMentorViewSet)
drouter.register(r'registrations', RegistrationViewSet)
drouter.register(r'faqs', FAQViewSet)
drouter.register(r'program-requests', ProgramRequestViewSet)
drouter.register(r'technologies', TechnologyViewSet)

urlpatterns = [
    path('', include(drouter.urls)),
]