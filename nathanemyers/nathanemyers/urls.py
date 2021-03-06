"""nathanemyers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin 

# imports for user uploads to work, docs recommend changing this for production
from django.conf import settings
from django.conf.urls.static import static

from . import views
 
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^at-map/', include('at_mapper.urls', namespace='at_mapper')),
    url(r'^nba/', include('nbapowerranks.urls', namespace='nba')),
    url(r'^projects/2015-2016-nba-power-rankings$', include('nbapowerranks.urls', namespace='nba')),
    url(r'^projects/$', views.ProjectsView.as_view(), name='projects'),
    url(r'^projects/2014-2015-nba-power-rankings$', views.NBALegacyView.as_view(), name='projects'),
    url(r'^about/', views.AboutView.as_view(), name='about'),
    url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
