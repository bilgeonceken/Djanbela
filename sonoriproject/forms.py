from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreateForm(UserCreationForm):
    class Meta:
        # fields = ("username", "email", "password1", "password2")
        model = User
        fields = UserCreationForm.Meta.fields + ("first_name",)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Nickname"
        self.fields["first_name"].label = "First Naaamoo"
