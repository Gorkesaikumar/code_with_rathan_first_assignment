from django.shortcuts import render
from .models import Course, Trainer, Student
# Create your views here.

def homepage(request):
    courses = Course.objects.all().count()
    trainers = Trainer.objects.all().count()
    students = Student.objects.all().count()
    return render(request, 'homepage.html', {'total_courses': courses, 'total_trainers': trainers, 'total_students': students})

def courses(request):
    course_list = Course.objects.all()
    return render(request, 'courses.html', {'courses': course_list})

def students(request):
    student_list = Student.objects.all()
    return render(request, 'students.html', {'students': student_list})

def trainers(request):
    trainer_list = Trainer.objects.all()
    return render(request, 'trainers.html', {'trainers': trainer_list})