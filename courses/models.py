from django.core.validators import FileExtensionValidator
from django.db import models
from utility.models import Utility


class Course(Utility):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Kurs nomi")
    description = models.TextField(null=True, blank=True, verbose_name="Kurs haqida malumot")
    image = models.ImageField(upload_to='course_images/', null=True, blank=True, verbose_name="Kurs rasmi",
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    weekly_hours = models.IntegerField(null=False, blank=False, verbose_name="Haftalik dars davomiyligi(soat)")
    duration_moths = models.IntegerField(null=False, blank=False, verbose_name="Kurs davomiyligi(oy)")
    total_hours = models.IntegerField(null=False, blank=False, verbose_name="Umumiy dars davomiyligi(soat)")
    price_per_moths = models.DecimalField(null=False, blank=False, verbose_name="Umumiy narxi(oylik)", max_digits=10, decimal_places=2)
    discount = models.DecimalField(null=True, blank=True, verbose_name="Chegrima(%)", max_digits=5, decimal_places=2)
    user_ai = models.BooleanField(null=True, blank=True, verbose_name="AI bilan ishlash", default=True)
    start_hour = models.TimeField(null=True, blank=True, verbose_name="Boshlanish vaqti(soat)")

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"

    def __str__(self):
        return self.title


class Mentor(Utility):
    first_name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Ism")
    last_name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Familiya")
    image = models.ImageField(upload_to='mentor_images/', null=True, blank=True, verbose_name="Mentor rasmi",
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    courses = models.ManyToManyField(Course, verbose_name="Kurslar", related_name="mentors")
    description = models.TextField(null=True, blank=True, verbose_name="Mentor haqida malumot")
    experience_years = models.IntegerField(null=False, blank=False, verbose_name="Tajribasi(yil)")
    student_count = models.IntegerField(null=False, blank=False, verbose_name="O'quvchi soni")

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Mentor"
        verbose_name_plural = "Mentorlar"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Portfolio(Utility):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Portfolio nomi")
    image = models.ImageField(upload_to='portfolio_images/', null=True, blank=True, verbose_name="Portfolio rasmi",
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    description = models.TextField(null=True, blank=True, verbose_name="Portfolio haqida malumot")
    mentor = models.ForeignKey(Mentor, on_delete=models.SET_NULL, null=True, blank=True, related_name="portfolios",
                               verbose_name="Mentor")
    url = models.URLField(null=True, blank=True, verbose_name="Portfolio sahifasi linki")

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolio"

    def __str__(self):
        return self.name

class CourseLessonVideo(Utility):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name="lesson_videos",
                               verbose_name="Kurs")
    video = models.FileField(upload_to='lesson_videos/', null=True, blank=True, verbose_name="Video",
                             validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mkv', 'avi'])])

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Video"

    def __str__(self):
        return f"{self.video}"

class FeedbackMentor(Utility):
    full_name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Ism")
    video = models.FileField(upload_to='feedback_videos/', null=True, blank=True, verbose_name="Video")
    couse = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name="feedbacks",
                               verbose_name="Kurs")
    mentor = models.ForeignKey(Mentor, on_delete=models.SET_NULL, null=True, blank=True, related_name="feedbacks",
                               verbose_name="Mentor")

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacklar"

    def __str__(self):
        return f"{self.full_name}"

class Registration(Utility):
    first_name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Ism")
    last_name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Familiya")
    phone_number = models.CharField(max_length=20, null=False, blank=False, verbose_name="Telefon raqami")
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name="registrations",
                               verbose_name="Kurs")

    class Meta:
        verbose_name = "Registratsiya"
        verbose_name_plural = "Registratsiyalar"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class FAQ(Utility):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Savol")
    description = models.TextField(null=False, blank=False, verbose_name="Javob")

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQ"

    def __str__(self):
        return f"{self.title}"
class ProgramRequest(Utility):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Ism")
    phone_number = models.CharField(max_length=20, null=False, blank=False, verbose_name="Telefon raqami")

    class Meta:
        verbose_name = "Program tayyorlash"
        verbose_name_plural = "Program tayyorlash"

    def __str__(self):
        return f"{self.name}"

class Technology(Utility):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Teg")
    image = models.ImageField(upload_to='technology_images/', null=True, blank=True, verbose_name="Teg rasmi",
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name="technologies",
                               verbose_name="Kurs")

    class Meta:
        verbose_name = "Teg"
        verbose_name_plural = "Teglar"

    def __str__(self):
        return f"{self.title}"



