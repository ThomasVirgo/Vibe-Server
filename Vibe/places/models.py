from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
# Restaurant model
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    is_viewable = models.BooleanField(default=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class RestaurantReview(models.Model):
    message = models.CharField(max_length=1000)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Review by {self.user_id} on {self.restaurant_id}'

# Event model
class Event(models.Model):
    name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=50)
    url = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    is_viewable = models.BooleanField(default=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_date = models.CharField(max_length=20)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class EventReview(models.Model):
    message = models.CharField(max_length=1000)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Review by {self.user_id} on {self.event_id}'