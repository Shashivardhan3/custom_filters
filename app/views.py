from django.shortcuts import render

# Create your views here.
def customfilters(request):
    d={'data':'Hai SHAHSi VArdhan'}
    return render(request, 'customfilters.html',d)