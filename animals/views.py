from django.shortcuts import render

from .models import Natimal

def homepage(request):
    return render(request, 'animals/index.html')

def mappage(request):
    return render(request, 'animals/map.html')

def countrydetail(request, country_slug):
    country = Natimal.objects.get(name_slug=country_slug)
    context = {"country": country}
    return render(request, 'animals/countrydetail.html', context)
