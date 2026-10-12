from django.contrib import admin
from Home.models import Review
from Home.models import CarDescription
from Home.models import PriceRange
from Home.models import CarType
from Home.models import Contact
from Home.models import Sedan
from Home.models import Luxury
from Home.models import Xuv


# Register your models here.
admin.site.register(Review)
admin.site.register(CarDescription)
admin.site.register(PriceRange)
admin.site.register(CarType)
admin.site.register(Contact)
admin.site.register(Sedan)
admin.site.register(Luxury)
admin.site.register(Xuv)

