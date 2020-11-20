from django.db import models
from django.utils import timezone


class TodoManager(models.Manager):
    def create_task(self, title, status):
        task = self.create(title=title, status=status, date=timezone.now)
        return task


class Todo(models.Model):
    STATUS = (
        ("incomplete", "INCOMPLETE"),
        ("paused", "PAUSED"),
        ("complete", "COMPLETE"),
    )

    title = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    status = models.TextField("status", choices=STATUS, default="incomplete")
