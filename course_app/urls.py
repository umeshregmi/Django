from django.urls import path
from course_app import views

urlpatterns = [
    path('/', views.home),
    path('home/', views.home)
]