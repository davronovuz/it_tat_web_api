from django.test import TestCase
from courses.models import Courses,Mentors,Feedback_Mentor,Registration,Portfolio,FAQ,ProgramRequest,Technology,Course_Video

class Course_VideoModelTest(TestCase):
    def setUp(self):
        self.course = Courses.objects.create(
            title="Python",
            description="Python kursi",
            image="path/to/image.jpg",
            duration_month=3,
            weekly_hours=5,
            duration_hours=10,
            price_per_month=1000,
            discount=10,
            user_ai=True
        )

        self.video = Course_Video.objects.create(
            title="Video nomi",
            course=self.course,
            video="path/to/video.mp4"
        )

    def test_video_creation(self):
        self.assertEqual(self.video.title, "Video nomi")
        self.assertEqual(self.video.course, self.course)
        self.assertEqual(self.video.video, "path/to/video.mp4")
        self.assertEqual(self.video.course.title, "Python")

    def test_video_str_method(self):
        self.assertEqual(str(self.video), "Video nomi")

class CoursesModelTest(TestCase):
    def setUp(self):
        self.course = Courses.objects.create(
            title="Python",
            description="Python kursi",
            image="path/to/image.jpg",
            duration_month=3,
            weekly_hours=5,
            duration_hours=10,
            price_per_month=1000,
            discount=10,
            user_ai=True
        )

    def test_course_creation(self):
        self.assertEqual(self.course.title, "Python")
        self.assertEqual(self.course.description, "Python kursi")
        self.assertEqual(self.course.image, "path/to/image.jpg")
        self.assertEqual(self.course.duration_month, 3)
        self.assertEqual(self.course.weekly_hours, 5)
        self.assertEqual(self.course.duration_hours, 10)
        self.assertEqual(self.course.price_per_month, 1000)
        self.assertEqual(self.course.discount, 10)
        self.assertTrue(self.course.user_ai)

    def test_course_str_method(self):
        self.assertEqual(str(self.course), "Python")


class MentorsModelTest(TestCase):
    def setUp(self):
        self.course = Courses.objects.create(
            title="Python",
            description="Python kursi",
            image="path/to/image.jpg",
            duration_month=3,
            weekly_hours=5,
            duration_hours=10,
            price_per_month=1000,
            discount=10,
            user_ai=True,
        )
        self.mentor = Mentors.objects.create(
            first_name="Asilbek",
            last_name="Husanov",
            description="Python Developer",
            experience=5,
            image="path/to/image.jpg",
            count_students=10
        )
        self.mentor.courses.add(self.course)

    def test_mentor_creation(self):
        self.assertEqual(self.mentor.first_name, "Asilbek")
        self.assertEqual(self.mentor.last_name, "Husanov")
        self.assertEqual(self.mentor.description, "Python Developer")
        self.assertEqual(self.mentor.experience, 5)
        self.assertEqual(self.mentor.image, "path/to/image.jpg")
        self.assertIn(self.course, self.mentor.courses.all())
        self.assertEqual(self.mentor.count_students, 10)


    def test_mentor_str_method(self):
        self.assertEqual(str(self.mentor), "Asilbek Husanov")


class Feedback_MentorModelTest(TestCase):
    def setUp(self):
        self.course = Courses.objects.create(
            title="Python",
            description="Python kursi",
            image="path/to/image.jpg",
            duration_month=3,
            weekly_hours=5,
            duration_hours=10,
            price_per_month=1000,
            discount=10,
            user_ai=True
        )

        self.mentor = Mentors.objects.create(
            first_name="Asilbek",
            last_name="Husanov",
            description="Python Developer",
            experience=5,
            image="path/to/image.jpg",
            count_students=10
        )

        self.feedback = Feedback_Mentor.objects.create(
            mentor=self.mentor,
            course=self.course,
            full_name="John Doe",
            video="path/to/video.mp4",
            feedback_text="Great mentor!"
        )

    def test_feedback_mentor_creation(self):
        self.assertEqual(self.feedback.mentor, self.mentor)
        self.assertEqual(self.feedback.course, self.course)
        self.assertEqual(self.feedback.full_name, "John Doe")
        self.assertEqual(self.feedback.video, "path/to/video.mp4")
        self.assertEqual(self.feedback.feedback_text, "Great mentor!")

    def test_feedback_mentor_str_method(self):
        self.assertEqual(str(self.feedback), "John Doe - Asilbek Husanov")


class RegistrationModelTest(TestCase):
    def setUp(self):
        self.course = Courses.objects.create(
            title="Python",
            description="Python kursi",
            image="path/to/image.jpg",
            duration_month=3,
            weekly_hours=5,
            duration_hours=10,
            price_per_month=1000,
            discount=10,
            user_ai=True
        )

        self.registration = Registration.objects.create(
            name="John Doe",
            course=self.course,
            phone_number="+990(99)999-88-99",
        )

    def test_registration_creation(self):
        self.assertEqual(self.registration.name, "John Doe")
        self.assertEqual(self.registration.course, self.course)
        self.assertEqual(self.registration.phone_number, "+998(99)999-88-99")
        self.assertEqual(self.registration.course.title, "Python")

    def test_registration_str_method(self):
        self.assertEqual(str(self.registration), "John Doe - Python")


class PortfolioModelTest(TestCase):
    def setUp(self):
        self.mentor = Mentors.objects.create(
            first_name="Asilbek",
            last_name="Husanov",
            description="Python Developer",
            experience=5,
            count_students=10
        )

        self.portfolio = Portfolio.objects.create(
            mentor=self.mentor,
            name="My Portfolio",
            image="path/to/image.jpg",
            url="https://example.com/portfolio",
            description="This is my portfolio."
        )

    def test_portfolio_creation(self):
        self.assertEqual(self.portfolio.mentor, self.mentor)
        self.assertEqual(self.portfolio.name, "My Portfolio")
        self.assertEqual(self.portfolio.image, "path/to/image.jpg")
        self.assertEqual(self.portfolio.url, "https://example.com/portfolio")
        self.assertEqual(self.portfolio.description, "This is my portfolio.")

    def test_portfolio_str_method(self):
        self.assertEqual(str(self.portfolio), "My Portfolio")


class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            title="Question 1",
            description="Answer 1"
        )

    def test_faq_creation(self):
        self.assertEqual(self.faq.title, "Question 1")
        self.assertEqual(self.faq.description, "Answer 1")

    def test_faq_str_method(self):
        self.assertEqual(str(self.faq), "Question 1")


class ProgramRequestModelTest(TestCase):
    def setUp(self):
        self.program_request = ProgramRequest.objects.create(
            name="John Doe",
            phone_number="+998(99)999-88-99",
        )

    def test_program_request_creation(self):
        self.assertEqual(self.program_request.name, "John Doe")
        self.assertEqual(self.program_request.phone_number, "+998(99)999-88-99")

    def test_program_request_str_method(self):
        self.assertEqual(str(self.program_request), "John Doe - +998(99)999-88-99")


class TechnologyModelTest(TestCase):
    def setUp(self):
        self.course = Courses.objects.create(
            title="Python",
            description="Python kursi",
            image="path/to/image.jpg",
            duration_month=3,
            weekly_hours=5,
            duration_hours=10,
            price_per_month=1000,
            discount=10,
            user_ai=True
        )

        self.technology = Technology.objects.create(
            title="Python",
            course=self.course,
            image="path/to/image.jpg",
        )

    def test_technology_creation(self):
        self.assertEqual(self.technology.title, "Python")
        self.assertEqual(self.technology.course, self.course)
        self.assertEqual(self.technology.image, "path/to/image.jpg")
        self.assertEqual(self.technology.course.title, "Python")