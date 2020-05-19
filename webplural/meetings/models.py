from django.db import models
from datetime import time
# Create your models here.
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time=models.TimeField(default=time(9))
    duration=models.IntegerField(default=1)


    def __str__(self):
        return f"{self.title} on {self.start_time} at {self.date}"
class room(models.Model):
    name=models.CharField(max_length=100)
    floor=models.IntegerField()
    number=models.IntegerField()

    def __str__(self):
        return f"{self.name} on floor {self.floor} at room {self.room}"





