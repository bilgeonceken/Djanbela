from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#
class Event(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    competitors = models.ManyToManyField(User)


    def __str__(self):
        return self.title

    class Meta:
        abstract = True
        ordering = ['-date',]


class ParkourEvent(Event):
    description = models.TextField()
    is_active = models.BooleanField(default=True)

class RunningEvent(Event):
    pass
