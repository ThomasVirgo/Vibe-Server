from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework import status
import requests
import os

PLACES_BASE_URL = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
PLACES_API_KEY = os.getenv('PLACES_API_KEY')


# Create your views here.

@api_view()
def index(request):
    return Response({"hello":"world"})

@api_view()
@renderer_classes([JSONRenderer])
def get_restaurants(request, query):
    url = f'{PLACES_BASE_URL}query={query}&type=restaurant&key={PLACES_API_KEY}'
    r = requests.get(url)
    return Response(r.json())
