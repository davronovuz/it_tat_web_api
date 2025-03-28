from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import (
    TechnologyViewSet, CourseViewSet, PortfolioViewSet, MentorViewSet, 
    CourseLessonVideoViewSet, FeedbackMentorViewSet, RegistrationViewSet, 
    FAQViewSet, ProgramRequestViewSet,HomeAPIView
)

router = DefaultRouter()
router.register(r'technologies', TechnologyViewSet, basename='technology')
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'portfolios', PortfolioViewSet, basename='portfolio')
router.register(r'mentors', MentorViewSet, basename='mentor')
router.register(r'course-lesson-videos', CourseLessonVideoViewSet, basename='course-lesson-video')
router.register(r'feedback-mentors', FeedbackMentorViewSet, basename='feedback-mentor')
router.register(r'registrations', RegistrationViewSet, basename='registration')
router.register(r'faqs', FAQViewSet, basename='faq')
router.register(r'program-requests', ProgramRequestViewSet, basename='program-request')

urlpatterns = [
    path('', HomeAPIView.as_view(), name='home'),
    path('api', include(router.urls)),
]