from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    reg_no = models.CharField(max_length=9)
    level = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id


class Course(models.Model):
    course_name = models.CharField(max_length=200)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    semester = models.IntegerField()
    enrollment_key = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name


class Enrollment(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_id


class Grade(models.Model):
    CAT = 'cat'
    EXAM = 'exam'
    ASSESSMENT_TYPES = (
        (CAT, 'cat'),
        (EXAM, 'quiz'),
    )
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.FloatField
    out_of = models.FloatField
    assessment_type = models.CharField(max_length=50, choices=ASSESSMENT_TYPES, default= CAT)
    done_on = models.DateField
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_requests_created')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_id