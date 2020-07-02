from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Note(models.Model):
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to='note/')
    body = models.TextField()
    slug = models.SlugField()
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    edited_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
