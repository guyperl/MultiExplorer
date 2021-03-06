from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from views import (
    home, create_exchange
)

urlpatterns = [
    url(r'^$', home, name="exchange"),
    url(r'^onchain$', create_exchange, name="make_exchange")
]
