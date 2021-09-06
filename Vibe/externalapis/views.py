from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework import status
import requests
import os
import json

PLACES_BASE_URL = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
PHOTOS_BASE_URL = 'https://maps.googleapis.com/maps/api/place/photo?'
PLACES_DETAIL_URL = 'https://maps.googleapis.com/maps/api/place/details/json?'
PLACES_API_KEY = os.getenv('PLACES_API_KEY')


# Create your views here.

@api_view()
def index(request):
    return Response({"hello":"world"})

@api_view()
@renderer_classes([JSONRenderer])
def get_restaurants(request, query):
    '''
    Properties to include:
        - formatted_address
        - name
        - rating
        - photos.photo_reference then get the photo using this
        - place_id to get the website url
        - user_ratings_total
    '''
    url = f'{PLACES_BASE_URL}query={query}&type=restaurant&key={PLACES_API_KEY}'
    r = requests.get(url)
    results = r.json()['results']
    output = []
    for result in results:
        photo_reference = result['photos'][0]['photo_reference']
        filtered_result = {
            "name":result['name'],
            "address":result['formatted_address'],
            "rating":result['rating'],
            "photo_reference": photo_reference,
            "photo_url": f'{PHOTOS_BASE_URL}maxwidth=1400&maxheight=1400&photo_reference={photo_reference}&key={PLACES_API_KEY}',
            "place_id":result['place_id'],
            "total_ratings":result['user_ratings_total']
        }
        output.append(filtered_result)
    return Response(output)

@api_view()
@renderer_classes([JSONRenderer])
def get_website_link(request, id):
    url = f'{PLACES_DETAIL_URL}place_id={id}&fields=website&key={PLACES_API_KEY}'
    r= requests.get(url)
    r_dict = r.json()
    try:
        website = r_dict["result"]["website"]
    except:
        website = 'Not Available'
    return Response(website)