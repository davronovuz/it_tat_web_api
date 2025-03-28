from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import (
    Technology, Course, Portfolio, Mentor, CourseLessonVideo,
    FeedbackMentor, Registration, FAQ, ProgramRequest
)
from .serializers import (
    TechnologySerializer, CourseSerializer, PortfolioSerializer,
    MentorSerializer, CourseLessonVideoSerializer, FeedbackMentorSerializer,
    RegistrationSerializer, FAQSerializer, ProgramRequestSerializer
)
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIRequestFactory
import io
from PIL import Image

# Haqiqiy rasm faylini simulyatsiya qilish uchun yordamchi funksiya
def create_test_image():
    image = Image.new('RGB', (100, 100), color='red')
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='JPEG')
    return SimpleUploadedFile("test.jpg", img_byte_arr.getvalue(), content_type="image/jpeg")

class BaseTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()

class TechnologyTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.technology = Technology.objects.create(
            title="Python",
            image=create_test_image()
        )

    def test_create_technology(self):
        url = reverse('technology-list')
        data = {
            "title": "JavaScript",
            "image": create_test_image()
        }
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.content)
        self.assertEqual(Technology.objects.count(), 2)

    def test_retrieve_technology(self):
        url = reverse('technology-detail', args=[self.technology.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Python")
        self.assertIn("image_url", response.data)

    def test_serializer(self):
        request = self.factory.get('/')
        serializer = TechnologySerializer(self.technology, context={'request': request})
        data = serializer.data
        self.assertEqual(data['title'], "Python")
        self.assertTrue(data['image_url'].startswith('http://testserver/media/'))

class CourseTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.technology = Technology.objects.create(title="Python", image=create_test_image())
        self.course = Course.objects.create(
            title="Python Course",
            description="Learn Python",
            duration_months=3,
            weekly_hours=6,
            duration_hours=2,
            price_per_month=100.00,
            discount=10,
            uses_ai=True
        )
        self.course.technologies.add(self.technology)

    def test_create_course(self):
        url = reverse('course-list')
        data = {
            "title": "JavaScript Course",
            "description": "Learn JS",
            "duration_months": 4,
            "weekly_hours": 8,
            "duration_hours": 2,
            "price_per_month": "150.00",
            "discount": 5,
            "uses_ai": False,
            "technologies": [self.technology.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 2)

    def test_retrieve_course(self):
        url = reverse('course-detail', args=[self.course.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Python Course")
        self.assertEqual(response.data['price_per_month'], '100.00')

class PortfolioTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.portfolio = Portfolio.objects.create(
            name="Web App",
            description="A web application",
            url="https://example.com",
            image=create_test_image()
        )

    def test_create_portfolio(self):
        url = reverse('portfolio-list')
        data = {
            "name": "Mobile App",
            "description": "A mobile app",
            "url": "https://mobile.com",
            "image": create_test_image()
        }
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.content)

    def test_retrieve_portfolio(self):
        url = reverse('portfolio-detail', args=[self.portfolio.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Web App")

class MentorTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.course = Course.objects.create(
            title="Python Course",
            price_per_month=100.00,
            duration_months=3,
            weekly_hours=6,
            duration_hours=2
        )
        self.portfolio = Portfolio.objects.create(name="Web App", image=create_test_image())
        self.mentor = Mentor.objects.create(
            first_name="John",
            last_name="Doe",
            description="Experienced mentor",
            experience_years=5,
            students_count=50,
            image=create_test_image()
        )
        self.mentor.courses.add(self.course)
        self.mentor.portfolios.add(self.portfolio)

    def test_retrieve_mentor(self):
        url = reverse('mentor-detail', args=[self.mentor.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['full_name'], "John Doe")

class CourseLessonVideoTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.course = Course.objects.create(
            title="Python Course",
            price_per_month=100.00,
            duration_months=3,
            weekly_hours=6,
            duration_hours=2
        )
        self.video = CourseLessonVideo.objects.create(
            title="Lesson 1",
            course=self.course,
            video=SimpleUploadedFile("lesson1.mp4", b"fake_video_content", content_type="video/mp4")
        )

    def test_retrieve_video(self):
        url = reverse('course-lesson-video-detail', args=[self.video.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Lesson 1")

class FeedbackMentorTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.mentor = Mentor.objects.create(
            first_name="John",
            last_name="Doe",
            experience_years=5,
            students_count=50,
            image=create_test_image()
        )
        self.feedback = FeedbackMentor.objects.create(
            mentor=self.mentor,
            full_name="Alice",
            feedback_text="Great mentor!",
            video=SimpleUploadedFile("feedback.mp4", b"fake_video_content", content_type="video/mp4")
        )

    def test_retrieve_feedback(self):
        url = reverse('feedback-mentor-detail', args=[self.feedback.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['full_name'], "Alice")

class RegistrationTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.course = Course.objects.create(
            title="Python Course",
            price_per_month=100.00,
            duration_months=3,
            weekly_hours=6,
            duration_hours=2
        )
        self.registration = Registration.objects.create(
            name="Bob",
            phone_number="+998901234567",
            course=self.course
        )

    def test_create_registration(self):
        url = reverse('registration-list')
        data = {
            "name": "Charlie",
            "phone_number": "+998901234568",
            "course": self.course.id  # To‘g‘ri course ID yuborilmoqda
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.content)
        self.assertEqual(Registration.objects.count(), 2)

class FAQTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.faq = FAQ.objects.create(question="What is this?", answer="An FAQ")

    def test_retrieve_faq(self):
        url = reverse('faq-detail', args=[self.faq.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['question'], "What is this?")

class ProgramRequestTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.request = ProgramRequest.objects.create(name="David", phone_number="+998901234569")

    def test_create_program_request(self):
        url = reverse('program-request-list')
        data = {"name": "Eve", "phone_number": "+998901234570"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class HomePageTestCase(BaseTestCase):
    def test_home_page(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertIn("swagger", data["endpoints"])
        self.assertIn("redoc", data["endpoints"])