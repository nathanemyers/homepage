from django.shortcuts import render
from . import google_map_api

# Create your views here.
def mapper(request):
    return render(request, 'mapper.html', {
        'version': '1.0',
        'map_api_key': google_map_api.map_api_key
        })
