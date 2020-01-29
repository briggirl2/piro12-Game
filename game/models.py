from django.conf import settings
from django.db import models


class Record(models.Model):
    INPUT_CHOICES = (
        ('가위', '가위'),
        ('바위', '바위'),
        ('보', '보')
    )

    user1 = models.CharField(max_length=50)
    user2 = models.CharField(max_length=50)
    user1_input = models.CharField(max_length=10, choices=INPUT_CHOICES)
    user2_input = models.CharField(max_length=10, choices=INPUT_CHOICES)
    result = models.CharField(max_length=30)
