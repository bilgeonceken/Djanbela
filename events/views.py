from django import forms
from django.views import generic
from django.contrib.admin import widgets
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy

from . import models
from . import forms

class ParkourCreateView(generic.CreateView):
    model = models.ParkourEvent
    template_name = "events/parkour_create.html"
    form_class = forms.ParkourEventForm
