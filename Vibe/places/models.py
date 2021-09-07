from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
# Restaurant model
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.CharField(max_length=250)
    place_id = models.CharField(max_length=250)
    address= models.CharField(max_length=250)
    is_viewable = models.BooleanField(default=True)
    rating = models.DecimalField(max_digits = 2, decimal_places = 1)
    total_ratings = models.IntegerField()
    username = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    category = models.CharField(max_length=50, default='restaurant')

    def __str__(self):
        return f'{self.name}'

class RestaurantReview(models.Model):
    message = models.CharField(max_length=1000)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    username = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Review by {self.username} on {self.restaurant_id}'

# Event model
class Event(models.Model):
    event_name = models.CharField(max_length=250)
    venue_name = models.CharField(max_length=250)
    venue_address = models.CharField(max_length=250)
    venue_type = models.CharField(max_length=250)
    photo_url = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    event_type = models.CharField(max_length=50)
    link = models.CharField(max_length=250)
    entry_price = models.DecimalField(max_digits=6, decimal_places=2)
    starts_at = models.CharField(max_length=20)
    ends_at = models.CharField(max_length=20)
    main_artist = models.CharField(max_length=400)
    main_genre = models.CharField(max_length=400)
    is_viewable = models.BooleanField(default=True)
    username = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default='event')

    def __str__(self):
        return f'{self.event_name}'


class EventReview(models.Model):
    message = models.CharField(max_length=1000)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    username = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Review by {self.username} on {self.event_id}'