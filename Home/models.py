from django.db import models

# Create your models here.

class Review(models.Model):
    rating = models.CharField(max_length=10)
    description = models.TextField()
    fullname = models.CharField(max_length=50)
    place = models.CharField(max_length=50)

    def __str__(self):
        return self.fullname