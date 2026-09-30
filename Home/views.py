from django.shortcuts import render, HttpResponse
from Home.models import Review
from Home.models import CarDescription
from Home.models import Gallery
from Home.models import PriceRange
from Home.models import CarType

# Create your views here.
def index(request):
    cartypes = CarType.objects.all()
    priceranges = PriceRange.objects.all()
    cardescriptions = CarDescription.objects.all()
    reviews = Review.objects.all()
    gallerys = Gallery.objects.all()
    return render(request, 'index.html', {'reviews':reviews, 'cardescriptions':cardescriptions, 'gallerys':gallerys, 'priceranges':priceranges, 'cartypes':cartypes})