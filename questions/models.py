from django.db import models
from django.utils import timezone
from users.models import Teacher

class Question(models.Model):
    author = models.ForeignKey(Teacher, on_delete= models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
   

    date_posted = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(default=None)

    def __str__(self):
        return f'{self.title} by {self.author}'
