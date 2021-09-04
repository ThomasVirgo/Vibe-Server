from django.contrib import admin
from .models import Restaurant, RestaurantReview, Event, EventReview

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(RestaurantReview)
admin.site.register(Event)
admin.site.register(EventReview)