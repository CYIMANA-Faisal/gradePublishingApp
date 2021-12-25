from django.db import models
from django.contrib.auth.models import User


class School(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=200)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Course(models.Model):

    LEVEL_ONE = 'One'
    LEVEL_TWO = 'Two'
    LEVEL_THREE = 'Three'
    LEVEL_FOUR = 'Four'

    LEVEL = (
        (LEVEL_ONE, 'One'),
        (LEVEL_TWO, 'Two'),
        (LEVEL_THREE, 'Three'),
        (LEVEL_FOUR, 'Four'),
    )

    ONE = 'One'
    TWO = 'Two'
    THREE = 'Three'
    SEMESTER = (
        (ONE, 'One'),
        (TWO, 'Two'),
        (THREE, 'Three'),
    )
    code = models.CharField(max_length=200)
    level = models.CharField(max_length=50, choices=LEVEL)
    academic_year = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    semester = models.CharField(max_length=50, choices=SEMESTER)
    enrollment_key = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code


class Grade(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    cat = models.FloatField(default=0.00)
    exam = models.FloatField(default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)

