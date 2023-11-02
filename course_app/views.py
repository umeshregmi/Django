from django.shortcuts import render
import datetime
from course_app.models import Student

# Create your views here.
def home(request):
    return render(request, 'course_app/home.html')
