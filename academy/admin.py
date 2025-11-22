from django.contrib import admin
from . models import Course, Trainer, Student
# Register your models here

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'duration')
    search_fields = ('course_name',)

admin.site.register(Course, CourseAdmin)

class TrainerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'expertise')
    search_fields = ('first_name', 'last_name', 'email', 'expertise')
admin.site.register(Trainer, TrainerAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')

admin.site.register(Student, StudentAdmin)