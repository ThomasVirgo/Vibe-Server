from rest_framework import serializers
from .models import Restaurant, RestaurantReview

class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = "__all__"

class RestaurantReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestaurantReview
        fields = "__all__"