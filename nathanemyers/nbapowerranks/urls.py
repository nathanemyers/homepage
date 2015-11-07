from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^rankings/(?P<year>[0-9]+)/(?P<week>[0-9]+)', views.rankings)
        ]
