from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from Home.models import Review
from Home.models import CarDescription
from Home.models import Gallery
from Home.models import PriceRange
from Home.models import CarType
from Home.models import Contact
from urllib.parse import quote

# Create your views here.
def index(request):
    if request.method == "POST":
        model = request.POST.get("model_required")
        pickup = request.POST.get("pickup_date")
        rdate = request.POST.get("return_date")
        rental = request.POST.get("rental_type")
        name = request.POST.get("name")
        wpnumber = request.POST.get("whatsapp")
        pickup_location = request.POST.get("pickup_location")
        return_location = request.POST.get("return_location") 
        passengers = request.POST.get("passengers")
        notes = request.POST.get("notes")

        Contact.objects.create(model_required=model,pickup_date=pickup,return_date=rdate,rental_type=rental,name=name,whatsapp=wpnumber,notes=notes,pickup_location=pickup_location,return_location=return_location,passengers=passengers)
        
        #whatsapp number integration
        your_whatsapp = "917201891836"
        message = f"""NEW BOOKING INQUIRY - SAMAY CAR RENTAL

        Customer Name : {name}
        Whatsapp : {wpnumber}
        Car / Model : {model}
        Rental Type : {rental}
        Pickup - Date : {pickup}
        Return - Date : {rdate}
        Pickup - Location : {pickup_location}
        Return - Location : {return_location}
        Total Passengers : {passengers}
        Additional Information : {notes}
        """

        whatsapp_url = (
            f"https://wa.me/{your_whatsapp}"
            f"?text={quote(message)}"
        )

        return JsonResponse({
        "success": True,
        "whatsapp_url": whatsapp_url
    })
    cartypes = CarType.objects.all()
    priceranges = PriceRange.objects.all()
    cardescriptions = CarDescription.objects.all()
    reviews = Review.objects.all()
    gallerys = Gallery.objects.all()
    return render(request, 'index.html', {'reviews':reviews, 'cardescriptions':cardescriptions, 'gallerys':gallerys, 'priceranges':priceranges, 'cartypes':cartypes})