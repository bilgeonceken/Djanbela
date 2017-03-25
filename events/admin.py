from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

## I use this inline to show the user's parkours in user form in django admin
class ParkourEventInline(admin.TabularInline):
    model = models.ParkourEvent.competitors.through

@admin.register(models.ParkourEvent)
class ParkourEventAdmin(admin.ModelAdmin):
    fields = ("title", "description", "date", "time", "competitors", "is_active",)
    ## Normally there is a select multiple field in the form, which is pretty mush useless
    ## but with this you can VERY easily add or remove competitors
    admin.ModelAdmin.filter_horizontal = ("competitors",)


@admin.register(models.RunningEvent)
class RunningEventAdmin(admin.ModelAdmin):
    pass


## To register our inlined UserForm, First we must unregister the old one
admin.site.unregister(models.User)

## Now we can register ours
@admin.register(models.User)
class MyUserAdmin(UserAdmin):
    inlines = [
        ParkourEventInline,
    ]
