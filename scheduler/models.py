from django.db import models


# Create your models here.
class Event(models.Model):
    start_time = models.DateTimeField()
    duration = models.IntegerField()
    description = models.CharField(max_length=200)
    notes = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
