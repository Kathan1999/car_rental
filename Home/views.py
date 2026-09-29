from django.shortcuts import render, HttpResponse
from Home.models import Review

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    return render(request, 'index.html', {'reviews':reviews})