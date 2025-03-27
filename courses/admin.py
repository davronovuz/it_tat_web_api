from django.contrib import admin
from .models import Courses,Mentors,Feedback_Mentor,Registration,Portfolio,FAQ,ProgramRequest,Technology

# Register your models here.
admin.site.register(Courses)
admin.site.register(Mentors)
admin.site.register(Feedback_Mentor)
admin.site.register(Registration)
admin.site.register(Portfolio)
admin.site.register(FAQ)
admin.site.register(ProgramRequest)
admin.site.register(Technology)