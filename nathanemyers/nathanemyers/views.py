from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from zinnia.models import Entry

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'index.html'
    def get_queryset(self):
        """Return the last five published questions"""
        return Entry.objects.order_by('-start_publication')[:5]

