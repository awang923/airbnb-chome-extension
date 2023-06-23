from django.shortcuts import render
from django.http import JsonResponse
from .models import Listing

# Create your views here.
def get_listings(request):
    listings = Listing.objects.all().values()
    return JsonResponse({'listings': list(listings)})