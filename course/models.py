from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=200)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    semester = models.IntegerField()
    enrollment_key = models.CharField(max_length=10)