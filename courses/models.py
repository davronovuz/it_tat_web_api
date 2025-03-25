from django.core.validators import FileExtensionValidator
from django.db import models
from utility.models import Utility


class Course(Utility):
    title = models.CharField(max_length=255,null=False,blank=False,verbose_name="Kurs nomi")
    description = models.TextField(null=True,blank=True,verbose_name="Kurs haqida ma'lumot")
    duration_months = models.IntegerField(null=False,blank=False,verbose_name="Kurs davomiyligi (oy)")
    weekly_hours = models.IntegerField(null=False,blank=False,verbose_name="Xaftalik dars (soat)")
    duration_hours = models.IntegerField(null=False,blank=False,verbose_name="Dars davomiyligi (soat)")
    start_date = models.DateField(null=True,blank=True,verbose_name="Boshlanish sanasi")
    image = models.ImageField(upload_to="courses",null=True,blank=True,verbose_name="Kurs rasmi",
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'webp', 'svg'])])
    price_per_month = models.DecimalField(null=False,blank=False,verbose_name="Kursning narxi (oylik)",max_digits=10,decimal_places=2)
    discount = models.IntegerField(null=True,blank=True,verbose_name="Chegirma (%)")
    uses_ai = models.BooleanField(null=True,blank=True,verbose_name="Kursda AI foydalaniladimi ?",default=True)

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"
    def __str__(self):
        return self.title

class Mentor(Utility):
    first_name = models.CharField(max_length=255,null=False,blank=False,verbose_name="Ismi")
    last_name = models.CharField(max_length=255,null=False,blank=False,verbose_name="Familiyasi")
    image = models.ImageField(upload_to="mentors",null=True,blank=True,verbose_name="Mentor rasmi",
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'webp', 'svg'])])
    description = models.TextField(null=True,blank=True,verbose_name="Mentor haqida ma'lumot")
    courses = models.ManyToManyField(Course,verbose_name="Kurslar",related_name="mentors")
    experience_years = models.IntegerField(null=False,blank=False,verbose_name="Tajriba (yil)")
    students_count = models.IntegerField(null=False,blank=False,verbose_name="Mentorning mamnun o'quvchilar soni")

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Mentor"
        verbose_name_plural = "Mentorlar"
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Portfolio(Utility):
    name = models.CharField(max_length=255,null=False,blank=False,verbose_name="Portfolio nomi")
    image = models.ImageField(upload_to="portfolios",null=True,blank=True,verbose_name="Portfolio rasmi",
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'webp', 'svg'])])
    description = models.TextField(null=True,blank=True,verbose_name="Portfolio haqida ma'lumot")
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name="portfolios")
    url= models.URLField(null=True,blank=True,verbose_name="Portfolio link")

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"
    def __str__(self):
        return self.name

