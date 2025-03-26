from django.test import TestCase
from .models import Course, Mentor, Portfolio, CourseLessonVideo, FeedbackMentor, Registration, FAQ, ProgramRequest, Technology

class ModelTestCase(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Python Darslari",
            weekly_hours=5,
            duration_moths=3,
            total_hours=60,
            price_per_moths=100.00
        )
        self.mentor = Mentor.objects.create(
            first_name="Ali",
            last_name="Valiyev",
            experience_years=5,
            student_count=100
        )
        self.portfolio = Portfolio.objects.create(
            name="Web Portfolio",
            mentor=self.mentor
        )
        self.video = CourseLessonVideo.objects.create(
            course=self.course
        )
        self.feedback = FeedbackMentor.objects.create(
            full_name="Olimjon",
            couse=self.course,
            mentor=self.mentor
        )
        self.registration = Registration.objects.create(
            first_name="Olim",
            last_name="Aliyev",
            phone_number="+998901234567",
            course=self.course
        )
        self.faq = FAQ.objects.create(
            title="Darslar qaysi tilda?",
            description="Darslar o'zbek tilida olib boriladi."
        )
        self.program_request = ProgramRequest.objects.create(
            name="Javohir",
            phone_number="+998909876543"
        )
        self.technology = Technology.objects.create(
            title="Django",
            course=self.course
        )

    def test_models_creation(self):
        self.assertEqual(self.course.title, "Python Darslari")
        self.assertEqual(self.mentor.get_full_name(), "Ali Valiyev")
        self.assertEqual(self.portfolio.name, "Web Portfolio")
        self.assertEqual(self.feedback.full_name, "Olimjon")
        self.assertEqual(self.registration.first_name, "Olim")
        self.assertEqual(self.faq.title, "Darslar qaysi tilda?")
        self.assertEqual(self.program_request.name, "Javohir")
        self.assertEqual(self.technology.title, "Django")

