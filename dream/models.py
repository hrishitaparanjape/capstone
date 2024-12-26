from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Dream(models.Model):
    EMOTIONAL_STATES = [
        ('happy', 'Happy'),
        ('scared', 'Scared'),
        ('confused', 'Confused'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
        ('excited', 'Excited'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    emotional_state = models.CharField(max_length=10, choices=EMOTIONAL_STATES)

    def __str__(self):
        return f"{self.title} ({self.date})"