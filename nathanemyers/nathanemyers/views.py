from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from zinnia.models import Entry

version = '1.1'

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_post_list'
    def get_queryset(self):
        """Return the last five published posts"""
        return Entry.objects.order_by('-start_publication')[:5]
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['version'] = version
        return context

class ProjectsView(generic.TemplateView):
    template_name = 'projects/projects.html'
    def get_context_data(self, **kwargs):
        context = super(ProjectsView, self).get_context_data(**kwargs)
        context['version'] = version
        return context

class NBALegacyView(generic.TemplateView):
    template_name = 'projects/nba-legacy.html'
    def get_context_data(self, **kwargs):
        context = super(NBALegacyView, self).get_context_data(**kwargs)
        context['version'] = version
        return context

class AboutView(generic.TemplateView):
    template_name = 'about.html'
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['version'] = version
        return context

