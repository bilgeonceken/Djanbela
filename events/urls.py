from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r"create_parkour/$", views.ParkourCreateView.as_view(), name="create_parkour"),
    url(r"parkour/(?P<pk>\d+)/$", views.ParkourDetailView.as_view(), name="parkour_detail"),
    url(r"parkours/$", views.PastParkoursListView.as_view(), name="parkour_list"),
    url(r"^search/$", views.search,name="parkour_search"),
]
