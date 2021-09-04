from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Restaurant, RestaurantReview, Event
from .serializers import RestaurantSerializer, RestaurantReviewSerializer, EventSerializer
from django.http import Http404


# Create your views here.

# Restaurant views
class RestaurantList(APIView):
    # permission_classes = [IsAuthenticated,]
    def get(self, request, format=None):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
            serializer = RestaurantSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RestaurantDetail(APIView):

    def get_object(self, restaurant_id):
        try:
            return Restaurant.objects.get(pk=restaurant_id)
        except Restaurant.DoesNotExist:
            raise Http404

    def get(self, request, restaurant_id, format=None):
        restaurant = self.get_object(restaurant_id)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

    def put(self, request, restaurant_id, format=None):
        restaurant = self.get_object(restaurant_id)
        serializer = RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, restaurant_id, format=None):
        restaurant = self.get_object(restaurant_id)
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RestaurantReviewList(APIView):
    # permission_classes = [IsAuthenticated,]
    def get(self, request, format=None):
        reviews = RestaurantReview.objects.all()
        serializer = RestaurantReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
            serializer = RestaurantReviewSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RestaurantReviewDetail(APIView):

    def get_object(self, review_id):
        try:
            return RestaurantReview.objects.get(pk=review_id)
        except RestaurantReview.DoesNotExist:
            raise Http404

    def get(self, request, review_id, format=None):
        review = self.get_object(review_id)
        serializer = RestaurantReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request, review_id, format=None):
        review = self.get_object(review_id)
        serializer = RestaurantReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, review_id, format=None):
        review = self.get_object(review_id)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Event views
class EventList(APIView):
    # permission_classes = [IsAuthenticated,]
    def get(self, request, format=None):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
            serializer = EventSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)