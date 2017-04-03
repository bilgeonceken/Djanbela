from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    competitors = models.ManyToManyField(User, blank=True)


    def __str__(self):
        return self.title

    class Meta:
        abstract = True
        ordering = ['-date',]


class ParkourEvent(Event):
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
                    #namespace:func_name
        return reverse("events:parkour_detail", kwargs={"pk":self.pk})


class RunningEvent(Event):
    pass
