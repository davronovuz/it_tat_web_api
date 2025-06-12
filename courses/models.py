from django.core.validators import FileExtensionValidator
from django.db import models
from utility.models import Utility


class Technology(Utility):
    title=models.CharField(max_length=255,null=True,blank=True,verbose_name="title")
    image=models.ImageField(upload_to="Technoly/",null=True,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Technology"
        verbose_name_plural="Technologies"


class Course(Utility):
    title = models.CharField(max_length=255,null=False,blank=False,verbose_name="Kurs nomi")
    description = models.TextField(null=True,blank=True,verbose_name="Kurs haqida ma'lumot")
    duration_months = models.IntegerField(null=False,blank=False,verbose_name="Kurs davomiyligi (oy)")
    weekly_hours = models.IntegerField(null=False,blank=False,verbose_name="Xaftalik dars (kun)")
    duration_hours = models.IntegerField(null=False,blank=False,verbose_name="Dars davomiyligi (soat)")
    start_date = models.DateField(null=True,blank=True,verbose_name="Boshlanish sanasi")
    image = models.ImageField(upload_to="courses",null=True,blank=True,verbose_name="Kurs rasmi",
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'webp', 'svg'])])
    price_per_month = models.DecimalField(null=False,blank=False,verbose_name="Kursning narxi (oylik)",max_digits=10,decimal_places=2)
    discount = models.IntegerField(null=True,blank=True,verbose_name="Chegirma (%)")
    uses_ai = models.BooleanField(null=True,blank=True,verbose_name="Kursda AI foydalaniladimi ?",default=True)
    technologies = models.ManyToManyField(Technology,verbose_name="Tehnologiyalar",related_name="courses")
    
    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"
    def __str__(self):
        return self.title


class Portfolio(Utility):
    name = models.CharField(max_length=255,null=False,blank=False,verbose_name="Portfolio nomi")
    image = models.ImageField(upload_to="portfolios",null=True,blank=True,verbose_name="Portfolio rasmi",
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'webp', 'svg'])])
    description = models.TextField(null=True,blank=True,verbose_name="Portfolio haqida ma'lumot")
    url= models.URLField(null=True,blank=True,verbose_name="Portfolio link")

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"
    def __str__(self):
        return self.name

class Mentor(Utility):
    first_name = models.CharField(max_length=255,null=False,blank=False,verbose_name="Ismi")
    last_name = models.CharField(max_length=255,null=False,blank=False,verbose_name="Familiyasi")
    image = models.ImageField(upload_to="mentors",null=True,blank=True,verbose_name="Mentor rasmi",
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'webp', 'svg'])])
    description = models.TextField(null=True,blank=True,verbose_name="Mentor haqida ma'lumot")
    courses = models.ManyToManyField(Course,verbose_name="Kurslar",related_name="mentors")
    experience_years = models.IntegerField(null=False,blank=False,verbose_name="Tajriba (yil)")
    students_count = models.IntegerField(null=False,blank=False,verbose_name="Mentorning mamnun o'quvchilar soni")
    projects_part_count = models.IntegerField(default=0,verbose_name="Mentorning qatnashgan loyihalar soni")
    achievements_count = models.IntegerField(default=0,verbose_name="Mentorning yutuqlar soni")
    portfolios = models.ManyToManyField(Portfolio,verbose_name="Portfolios",related_name="mentors",null=True,blank=True)
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Mentor"
        verbose_name_plural = "Mentorlar"
    def __str__(self):
        return f"{self.first_name} {self.last_name}"




class CourseLessonVideo(Utility):
    title= models.CharField(max_length=255,null=True,blank=True,verbose_name="Dars nomi")
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name="lesson_videos",
                               verbose_name="Kurs")
    video = models.FileField(upload_to='lesson_videos/', null=True, blank=True, verbose_name="Video",
                             validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mkv', 'avi','mov', 'wmv', 'webm','flv'])])

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Video"


    def __str__(self):
        return f"{self.video}"








class FeedbackMentor(Utility):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Mentor")
    full_name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Foydalanuvchi ismi")
    video = models.FileField(
        upload_to="feedback_videos/",
        null=True, blank=True,
        verbose_name="Fikr-mulohaza videosi",
        validators=[FileExtensionValidator(allowed_extensions=["mp4", "mov", "avi", "mkv"])]
    )
    feedback_text = models.TextField(null=True, blank=True, verbose_name="Izoh (matn shaklida)")

    class Meta:
        db_table = "feedback_mentor"
        verbose_name = "Mentor haqida fikr"
        verbose_name_plural = "Mentorlar haqida fikrlar"


    def __str__(self):
        mentor_name = self.mentor.get_full_name() if self.mentor else "No Mentor"
        return f"{self.full_name} - {mentor_name}"


class Registration(Utility):
    name=models.CharField(max_length=255,null=False,blank=False,verbose_name="Ismn")
    phone_number=models.CharField(max_length=17, null=False,blank=False,unique=True)


    class Meta:
        verbose_name="Registration"
        verbose_name_plural="Registration"

    def __str__(self):
        return self.name





class FAQ(Utility):
    question=models.CharField(max_length=255,null=False,blank=False,verbose_name="title")
    answer=models.TextField(null=False,blank=False,verbose_name="Malumot")

    class Meta:
        verbose_name="FAQ"
        verbose_name_plural="FAQ"
    def __str__(self):
        return f"{self.question} - {self.answer}"


class ProgramRequest(Utility):
    name=models.CharField(max_length=255,null=False,blank=False)
    phone_number=models.CharField(max_length=17,null=False,blank=False,unique=True)


    class Meta:
        verbose_name="ProgramRequest"
        verbose_name_plural = "ProgramRequest"

    def __str__(self):
        return self.name
