from django import forms
from django.views import generic
from django.db.models import Q
from django.shortcuts import redirect, reverse, render
from django.core.urlresolvers import reverse_lazy
from django.contrib.admin import widgets

from braces.views import StaffuserRequiredMixin, LoginRequiredMixin

from . import models
from . import forms

class ParkourCreateView(LoginRequiredMixin, StaffuserRequiredMixin, generic.CreateView):
    model = models.ParkourEvent
    template_name = "events/parkour_create.html"
    form_class = forms.ParkourEventForm


##
## This view handles all AddUser-RemoveUser action on ParkourEvent
##
class ParkourDetailView(generic.DetailView):
    model = models.ParkourEvent
    template_name = "events/parkour_detail.html"

    ## i can delete this override, but i want to test if i user p.._related
    ## correct and it actually does something
    ## but i'm too lazy to install the toolbar for that
    def get_query_set(self):
        return self.model.objects.prefetch_related('competitors').all()

    ## process your request and
    ## redirects you where the fuck you come from
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            pmodel = models.ParkourEvent.objects.get(pk=kwargs["pk"])
            if (request.user in pmodel.competitors.all()) and request.POST.get("remove"):
                pmodel.competitors.remove(request.user)
            elif (request.user not in pmodel.competitors.all()) and request.POST.get("add"):
                pmodel.competitors.add(request.user)
                # return redirect(pmodel)
            # return redirect(pmodel)
            print(self.request.user.pk)
            return redirect(request.META["HTTP_REFERER"])
        else:
            # redirect(pmodel)
            return redirect(request.META["HTTP_REFERER"])

class PastParkoursListView(generic.ListView):
    template_name = "events/parkour_list.html"

    ## by default context_object_name = *modelname*_list
    context_object_name = "parkours"

    ## we can directly define a modal or query_set i guess
    ## but well... this works too, overriding stuff
    def get_queryset(self):
        return models.ParkourEvent.objects.filter()


def search(request):
    # gets the value of input box named "q"
    term = request.GET.get("q")
    # "i"contains. that i means make this case insensitive
    parkours = models.ParkourEvent.objects.filter(
        # tihs way we can search both titles and desc.s without them interrupting
        # each other. Q objects are entire queries on their own
        Q(title__icontains=term) | Q(description__icontains=term) | Q(date__icontains=term) )
    return render(request, "events/parkour_list.html", {"parkours": parkours})