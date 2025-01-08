from django.db import models
from users.models import User
from courses.models import Course

class Exam(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    duration_minutes = models.IntegerField()
    total_marks = models.IntegerField()

class ExamResult(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    score = models.IntegerField()
    feedback = models.TextField(blank=True, null=True)
