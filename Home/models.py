from django.db import models

# Create your models here.

class Review(models.Model):
    rating = models.CharField(max_length=10)
    description = models.TextField()
    fullname = models.CharField(max_length=50)
    place = models.CharField(max_length=50)

    def __str__(self):
        return self.fullname

class CarDescription(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/', blank=True, null=True)
    year = models.PositiveBigIntegerField()
    fuel_type = models.CharField(max_length=50)
    gair = models.CharField(max_length=50)
    seats_type = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField(default=0)
    km = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class PriceRange(models.Model):
    total_hours = models.CharField(max_length=20)
    price_from = models.IntegerField(default=0)
    price_to = models.IntegerField(default=0)
    total_days = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.total_hours

class CarType(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    days = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    model_required = models.CharField(max_length=100)
    pickup_date = models.DateField()
    return_date = models.DateField()
    rental_type = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=20)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + self.whatsapp
