from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from PIL import Image


class Daily(models.Model):
    date = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    grateful_for = models.JSONField(null=True, blank=True)
    thoughts = models.TextField(null=True, blank=True)
    daily_pic = models.ImageField(null=True, blank=True, upload_to='daily_pics')

    def get_absolute_url(self):
        return reverse('gratitude', kwargs={'pk': self.pk})

    def __str__(self):
        return f"Daily notes of {self.author.username}. Day: {self.date}."

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        try:
            img = Image.open(self.daily_pic.path)

            if img.height > 400 or img.width > 400:
                output_size = (400, 400)
                img.thumbnail(output_size)
                img.save(self.daily_pic.path)
        except ValueError:
            pass
