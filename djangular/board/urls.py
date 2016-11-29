"""Define urls for accessing our views."""
from django.conf.urls import url

from .api import CardView, ListView

urlpatterns = [
    url(r'^lists$', ListView.as_view()),
    url(r'^cards$', CardView.as_view())
]
