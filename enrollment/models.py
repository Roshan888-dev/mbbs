from django.db import models
from users.models import User
from courses.models import Course


class Enrollment(models.Model):
    student = models.ForeignKey(User, related_name='enrollments', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='enrollments', on_delete=models.CASCADE)
    enroll_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('active', 'Active'), ('completed', 'Completed'), ('dropped', 'Dropped')], default='active')

    class Meta:
        unique_together = ('student', 'course')  # Prevent multiple enrollments in the same course by the same student.

    def __str__(self):
        return f"{self.student.username} - {self.course.title}"
