from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User

# from django.contrib.auth.forms import UserCreationForm
from . import forms


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

## User's edit profile view
class UserProfileView(generic.DetailView, generic.UpdateView):
    fields = ("username", "first_name", "last_name", "email")
    template_name = "user_profile.html"
    success_url = "/accounts/profile"

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.pk)

class PublicProfileView(generic.DetailView):
    template_name = "public_profile.html"
    model = User

class HomeView(View):

    def get(self, request):
        return render(request, "home.html")