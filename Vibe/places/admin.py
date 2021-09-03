from django.contrib import admin
from .models import Restaurant, RestaurantReview

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(RestaurantReview)