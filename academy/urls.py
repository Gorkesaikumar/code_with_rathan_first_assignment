from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('academy/courses/', views.courses, name='courses'),
    path('academy/trainers/', views.trainers, name='trainers'),
    path('academy/students/', views.students, name='students'),
]
