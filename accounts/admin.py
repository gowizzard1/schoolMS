from django.contrib import admin
from .models import  SalaryGrade,School,TeachersInformation,Library,Login,Hostel,Classinformation,Subjects,Syllabus,\
    Routine,HumanResource,Assignment,ExamGrade,DataStudent
# Register your models here.
admin.site.register(School)
admin.site.register(SalaryGrade)
admin.site.register(TeachersInformation)
admin.site.register(Login)
admin.site.register(Classinformation)
admin.site.register(Subjects)
admin.site.register(Syllabus)
admin.site.register(HumanResource)
admin.site.register(Routine)
admin.site.register(Assignment)
admin.site.register(ExamGrade)
admin.site.register(DataStudent)