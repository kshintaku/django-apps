from django.db import models
from django.utils import timezone


class TodoManager(models.Manager):
    def create_task(self, title):
        task = self.create(title=title, date=timezone.now)
        return task


class Todo(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    complete = models.BooleanField("complete", blank=True, default=False)
    paused = models.BooleanField("paused", blank=True, default=False)
