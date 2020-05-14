from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = [
        ('STU', 'Student'),
        ('TEA', 'Teacher')
    ]
    userRole = models.CharField(
        max_length=3,
        choices=ROLE_CHOICES,
        default='STU'
    )

    def __str__(self):
        return f'{self.user.username} Profile'

