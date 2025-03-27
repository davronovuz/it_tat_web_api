from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import CourseViewSet


router = DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = router.urls


