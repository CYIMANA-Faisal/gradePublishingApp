from django.db import models
from django.contrib.auth.models import User
from department.models import Department
# Create your models here.


class Student(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    reg_no = models.CharField(max_length=9)
    level = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
