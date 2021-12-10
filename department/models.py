from django.db import models
from school.models import School
# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length= 200)
    school_id = models.ForeignKey(School, on_delete= models.CASCADE)