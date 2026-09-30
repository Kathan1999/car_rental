from django.contrib import admin
from Home.models import Review
from Home.models import CarDescription
from Home.models import Gallery
from Home.models import PriceRange
from Home.models import CarType

# Register your models here.
admin.site.register(Review)
admin.site.register(CarDescription)
admin.site.register(Gallery)
admin.site.register(PriceRange)
admin.site.register(CarType)