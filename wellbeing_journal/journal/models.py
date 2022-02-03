from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Daily(models.Model):
    date = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    grateful_for1 = models.TextField(default='')
    grateful_for2 = models.TextField(default='')
    grateful_for3 = models.TextField(default='')
    thoughts = models.TextField(default='')
    daily_pic = models.ImageField(default='nice_pic.jpg', upload_to='daily_pics')

    def __str__(self):
        return f"Daily notes of {self.author.username}. Day: {self.date}."
