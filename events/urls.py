from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r"create_parkour/$", views.ParkourCreateView.as_view(), name="create_parkour"),
]
