from django.core.validators import FileExtensionValidator
from django.db import models
from utility.models import Utility


class Course(Utility):
    title = models.CharField(max_length=255,null=False,blank=False,verbose_name="Kurs nomi")
    description = models.TextField(null=True,blank=True,verbose_name="Kurs haqida malumot")
    image = models.ImageField(upload_to='course_images/',null=True,blank=True,verbose_name="Kurs rasmi",
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png','webp','svg'])])
    weekly_hours = models.IntegerField(null=False,blank=False,verbose_name="Haftalik dars davomiyligi(soat)")
    duration_moths=models.IntegerField(null=False,blank=False,verbose_name="Dars davomiyligi(soat)")
    start_date=models.DateTimeField(null=True,blank=True,verbose_name="Boshlanish sanasi")
    total_hours=models.IntegerField(null=False,blank=False,verbose_name="Umumiy dars davomiyligi(soat)")
    price_per_moths=models.DecimalField(null=False,blank=False,verbose_name="Umumiy narxi(oylik)",max_digits=10,decimal_places=2)
    discount=models.DecimalField(null=True,blank=True,verbose_name="Chegrima(%)")
    user_ai=models.BooleanField(null=True,blank=True,verbose_name="AI bilan ishlash",default=True)


    class Meta:
        verbose_name="Kurs"
        verbose_name_plural="Kurslar"

    def __str__(self):
        return self.title


class Mentor(Utility):
    first_name=models.CharField(max_length=255,null=False,blank=False,verbose_name="Ismi")
    last_name=models.CharField(max_length=255,null=False,blank=False,verbose_name="Familyasi")
    image=models.ManyToManyField(upload_to="mentors",null=False,blank=True,verbose_name="Mentor rasmi",
                                 validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png','webp','svg'])])
    courses = models.ManyToManyField(Course, verbose_name="Kurslar", related_name="mentors")
    description = models.TextField(null=True, blank=True, verbose_name="Mentor haqida malumot")
    experience_years = models.IntegerField(null=False, blank=False, verbose_name="Tajribasi(yil)")
    student_count = models.IntegerField(null=False, blank=False, verbose_name="O'quvchi soni")

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


    class Meta:
        verbose_name= "Mentor"
        verbose_name_plular="Mentorlar"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Portfolio(Utility):
    name=models.CharField(max_length=255,null=False,blank=False,verbose_name="Portfolio nomi")
    image=models.ManyToManyField(upload_to="portfolios",null=False,blank=True,verbose_name="Portfolio rasmi",
                                 validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png','webp','svg'])])
    description = models.TextField(null=True,blank=True,verbose_name="POrtfolio haqida malumot")
    mentor=models.ForeignKey(Mentor,on_delete=models.CASCADE,related_name="portfolios")
    url=models.URLField(null=True,blank=True,verbose_name="Portfolio link")

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plular = "Portfolios"

    def __str__(self):
        return self.name


class Technology(Utility):
    title=models.CharField(max_length=255,null=True,blank=True,verbose_name="title")
    image=models.ImageField(upload_to="Technoly/",null=True,blank=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        verbose_name="Technology"
        verbose_name_plural="Technologies"



class Registration(Utility):
    name=models.CharField(max_length=255,null=False,blank=False,verbose_name="Ismn")
    phone_number=models.CharField(max_length=17, null=False,blank=False,unique=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=False,blank=False)


    class Meta:
        verbose_name="Registration"
        verbose_name_plural="Registration"

    def __str__(self):
        return self.name



class FeedbackMentor(Utility):
    full_name=models.CharField(max_length=255,null=False,blank=False,verbose_name="Ism")
    video=models.FileField(upload_to="feedback_video/",null=True,blank=True,verbose_name="VIdeolar")
    course=models.ForeignKey(Course,on_delete=models.SET_NULL,null=True,blank=True,verbose_name="Kurs")
    mentor=models.ForeignKey(Mentor,on_delete=models.SET_NULL,null=True,blank=True)

    class Meta:
        verbose_name="Feedback"
        verbose_name_plural="Feedback"
    def __str__(self):
        return self.full_name

class FAQ(Utility):
    title=models.CharField(max_length=255,null=False,blank=False,verbose_name="title")
    description=models.TextField(null=False,blank=False,verbose_name="Malumot")

    class Meta:
        verbose_name="FAQ"
        verbose_name_plural="FAQ"
    def __str__(self):
        return self.title

class ProgramRequest(Utility):
    name=models.CharField(max_length=255,null=False,blank=False)
    phone_number=models.CharField(max_length=17,null=False,blank=False,unique=True)


    class Meta:
        verbose_name="ProgramRequest"
        verbose_name_plural = "ProgramRequest"

    def __str__(self):
        return self.name


class Course_lesson_video(Utility):
    video=models.FileField(upload_to="course_lesson/",null=True,blank=True,verbose_name="videolar")
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True)


    class Meta:
        verbose_name="Course_lesson_video"
        verbose_name_plural="Course_lesson_video"

    def __str__(self):
        return self.video