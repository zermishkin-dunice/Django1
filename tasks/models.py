from django.conf import settings
from django.db import models
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=40, null=True)
    desc = models.TextField()
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title