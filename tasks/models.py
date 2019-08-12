from django.conf import settings
from django.db import models
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=40, null=False)
    desc = models.TextField(null=False)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title