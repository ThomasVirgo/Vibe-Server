from django.contrib import admin
from .models import Restaurant, RestaurantReview, Event

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(RestaurantReview)
admin.site.register(Event)