from django.db import models

# Create your models here.
class Listing(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    reviews = models.TextField()

    def __str__(self):
        return self.name