from django import forms

from . import models

class ParkourEventForm(forms.ModelForm):

    date = forms.DateField(widget=forms.DateInput(attrs={"class": "datepicker form-control"}))

    class Meta:
        model = models.ParkourEvent
        fields = [
            "title",
            "description",
            "date",
            "time",
        ]
