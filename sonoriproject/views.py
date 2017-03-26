from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.forms import UserCreationForm
from . import forms
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User


## UserCreationFrom is a default modelform provided by auth module
## to make usercreation easily. we however modiefied it a bit in forms.py
## and will use it to have control on things
class SignupView(generic.CreateView):
    # form_class = UserCreationForm
    ## We use modified version of UserCreationForm
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class UserListView(generic.ListView):
    ## for user in object_list print user
    ## this is how listview rolls in template
    model = User
    template_name = "user_list.html"
