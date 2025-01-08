from django.db import models
from users.models import User

class Notification(models.Model):
    user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=[('read', 'Read'), ('unread', 'Unread')], default='unread')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}"
