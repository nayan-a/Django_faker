import os
import django
#Run Administrative Tasks
os.environ.setdefault('DJANGO_SETTINGS_MODULE','fakeproject.settings')
django.setup()
from faker import Faker
from myApp.models import Student
f=Faker()
def generate_data(n):
    for i in range(n):
        fname=f.name()
        froll=f.random_int(min=1,max=100)
        fmarks=f.random_int(min=1,max=100)
        fdob=f.date_of_birth()
        femail=f.email()
        s=Student.objects.get_or_create(name=fname,rollno=froll,marks=fmarks,dob=fdob,email=femail)
generate_data(20)