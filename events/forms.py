from django import forms

from . import models

class ParkourEventForm(forms.ModelForm):

    ### I've customized the classes of the field in another way (ln. 28)
    ### but i'll keep this line as a reference
    # date = forms.DateField(widget=forms.DateInput(attrs={"class": "datepicker form-control"}))

    class Meta:
        model = models.ParkourEvent
        fields = [
            "title",
            "description",
            "date",
            "time",
        ]

        # labels = {
        #     "time":"Zaman"
        # }

        placeholders = {
            "time": "H:M"
        }

        widgets = {
                # ## It may not be the correct approach to do attrs in here
                # ## But is definately the easier one at the moment. 
                # Check parkour_create.html
            "date": forms.DateInput(attrs={"class": "datepicker form-control"})
        }
