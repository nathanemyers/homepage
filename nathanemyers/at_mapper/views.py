from django.shortcuts import render

# Create your views here.
def mapper(request):
    return render(request, 'mapper.html', {
        'version': '1.0'
        })
