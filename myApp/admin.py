from django.contrib import admin
from myApp.models import Student
# Register your models here.
class StudenAdmin(admin.ModelAdmin):
    l=['name','rollno','marks','dob','email']
admin.site.register(Student,StudenAdmin)