from django.shortcuts import render
import datetime
from course_app.models import Student

# Create your views here.
def home(request):
    student = Student.objects.all()[0]
    return render(request, 'course_app/home.html', {'student': student})
