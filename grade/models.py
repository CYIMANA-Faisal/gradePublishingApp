from django.contrib.auth.models import User
from django.db import models
from course.models import Course


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
