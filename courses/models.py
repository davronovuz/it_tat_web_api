from django.db import models
from utility.models import Utility
from django.core.validators import FileExtensionValidator

class Courses(Utility):
    title = models.CharField(max_length=255, null=False, blank=False,verbose_name="Kurs nomi")
    description = models.TextField(null=True, blank=True,verbose_name="Kurs haqida ma'lumot")
    duration_month = models.IntegerField(null=False, blank=False,verbose_name="Kurs davomiyligi (oy)")
    weekly_hours = models.IntegerField(null=False, blank=False,verbose_name="Xafta davomiyligi (kun)")
    duration_hours = models.IntegerField(null=False, blank=False,verbose_name="Dars davomiyligi (soat)")
    image = models.ImageField(upload_to="images/", null=True, blank=True,verbose_name="Kurs rasmi",
                              validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png","webp","svg"])])
    price_per_month = models.DecimalField(null=False, blank=False,verbose_name="Kurs narxi (oylik)",max_digits=10, decimal_places=2)
    discount = models.IntegerField(default=0, null=True, blank=True, verbose_name="Chegirma(%)")
    user_ai=models.BooleanField(null=True, blank=True,verbose_name="Kursda AI foydalaniladi")



    class Meta:
        db_table = "courses"
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"

    def __str__(self):
        return self.title

class Mentors(Utility):
    first_name = models.CharField(max_length=255, null=False, blank=False,verbose_name="Mentor ismi")
    last_name = models.CharField(max_length=255, null=False, blank=False,verbose_name="Mentor familiyasi")
    image = models.ImageField(upload_to="mentors/", null=True, blank=True,verbose_name="Mentor rasmi",
                              validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png","webp","svg"])])
    description = models.TextField(null=True, blank=True,verbose_name="Mentor haqida ma'lumot")
    courses = models.ManyToManyField(Courses,verbose_name="Kurslar",related_name="mentors")
    experience = models.IntegerField(null=False, blank=False,verbose_name="Mentor tajribasi (Yil)")
    count_students = models.IntegerField(null=False, blank=False,verbose_name="Mentorning mamnun studentlar soni")


    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = "mentors"
        verbose_name = "Mentor"
        verbose_name_plural = "Mentorlar"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Portfolio(Utility):
    name = models.CharField(max_length=255, null=False, blank=False,verbose_name="Portfolio nomi")
    image = models.ImageField(upload_to="portfolios/", null=True, blank=True,verbose_name="Portfolio rasmi",
                              validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png","webp","svg"])])
    url = models.URLField(null=False, blank=False,verbose_name="Portfolio linki")
    description = models.TextField(null=True, blank=True,verbose_name="Portfolio haqida ma'lumot")
    mentor = models.ForeignKey(Mentors, on_delete=models.CASCADE, null=True, blank=True,verbose_name="Mentor")


    class Meta:
        db_table = "portfolios"
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfoliolar"

    def __str__(self):
        return self.name

class Feedback_Mentor(Utility):
    mentor = models.ForeignKey(Mentors, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Mentor")
    full_name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Foydalanuvchi ismi")
    video = models.FileField(
        upload_to="feedback_videos/",
        null=True, blank=True,
        verbose_name="Fikr-mulohaza videosi",
        validators=[FileExtensionValidator(allowed_extensions=["mp4", "mov", "avi", "mkv"])]
    )
    feedback_text = models.TextField(null=True, blank=True, verbose_name="Izoh (matn shaklida)")
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Kurs")

    class Meta:
        db_table = "feedback_mentor"
        verbose_name = "Mentor haqida fikr"
        verbose_name_plural = "Mentorlar haqida fikrlar"


    def __str__(self):
        mentor_name = self.mentor.get_full_name() if self.mentor else "No Mentor"
        return f"{self.full_name} - {mentor_name}"


class Registration(Utility):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Ism")
    phone_number = models.CharField(max_length=20, null=False, blank=False, verbose_name="Telefon raqami")
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Kurs")

    class Meta:
        db_table = "registration"
        verbose_name = "Ro‘yxatdan o‘tish"
        verbose_name_plural = "Ro‘yxatdan o‘tishlar"

    def __str__(self):
        return f"{self.name} - {self.course.title}"


class FAQ(Utility):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Savol")
    description = models.TextField(null=False, blank=False, verbose_name="Javob")

    class Meta:
        db_table = "faq"
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.title


class ProgramRequest(Utility):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Ism")
    phone_number = models.CharField(max_length=20, null=False, blank=False, verbose_name="Telefon raqami")

    class Meta:
        db_table = "program_requests"
        verbose_name = "Dastur so‘rovi"
        verbose_name_plural = "Dastur so‘rovlari"

    def __str__(self):
        return f"{self.name} - {self.phone_number}"


class Technology(Utility):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Texnologiya nomi")
    image = models.ImageField(upload_to="technologies/", null=True, blank=True, verbose_name="Texnologiya rasmi",
                              validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "webp", "svg"])])
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name="Kurs", related_name="technologies")

    class Meta:
        db_table = "technologies"
        verbose_name = "Texnologiya"
        verbose_name_plural = "Texnologiyalar"

    def __str__(self):
        return self.title

class Course_Video(Utility):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Video nomi")
    video = models.FileField(upload_to="videos/", null=False, blank=False, verbose_name="Video")
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name="Kurs", related_name="videos")

    class Meta:
        db_table = "course_videos"
        verbose_name = "Video"
        verbose_name_plural = "Videos"

    def __str__(self):
        return self.title