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


#TODO: This is only view, no template, no url.
class PastParkoursListView(generic.ListView):
    template_name = "events/pastparkour_list.html"

    ## by default context_object_name = *modelname*_list
    context_object_name = "pastparkours"

    ## we can directly define a modal or query_set i guess
    ## but well... this works too, overriding stuff
    def get_queryset(self):
        return models.ParkourEvent.objects.filter(is_active=False)


#TODO: This is only view, no template, no url.
class ActiveEventListView(generic.ListView):
    template_name = "activeparkour_list.html"

    def get_queryset(self):
        return models.ParkourEvent.objects.filter(is_active=True)
