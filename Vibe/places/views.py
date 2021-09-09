from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Restaurant, RestaurantReview, Event, EventReview
from .serializers import RestaurantSerializer, RestaurantReviewSerializer, EventSerializer, EventReviewSerializer
from django.http import Http404
from django.shortcuts import get_object_or_404


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

class GetRestaurantReviews(APIView):

    def get(self, request, restaurant_id, format=None):
        reviews = RestaurantReview.objects.filter(restaurant_id = restaurant_id)
        serializer = RestaurantReviewSerializer(reviews, many=True)
        return Response(serializer.data)

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


class EventDetail(APIView):

    def get_object(self, event_id):
        try:
            return Event.objects.get(pk=event_id)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, event_id, format=None):
        event = self.get_object(event_id)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def put(self, request, event_id, format=None):
        event = self.get_object(event_id)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, event_id, format=None):
        event = self.get_object(event_id)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Event Review views
class EventReviewList(APIView):
    # permission_classes = [IsAuthenticated,]
    def get(self, request, format=None):
        reviews = EventReview.objects.all()
        serializer = EventReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
            serializer = EventReviewSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventReviewDetail(APIView):

    def get_object(self, review_id):
        try:
            return EventReview.objects.get(pk=review_id)
        except EventReview.DoesNotExist:
            raise Http404

    def get(self, request, review_id, format=None):
        review = self.get_object(review_id)
        serializer = EventReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request, review_id, format=None):
        review = self.get_object(review_id)
        serializer = EventReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, review_id, format=None):
        review = self.get_object(review_id)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetEventReviews(APIView):

    def get(self, request, event_id, format=None):
        reviews = EventReview.objects.filter(event_id = event_id)
        serializer = EventReviewSerializer(reviews, many=True)
        return Response(serializer.data)

# Get all saved restaurants and events for a given user
class GetRestaurantsByUser(APIView):
    def get(self, request, username, format=None):
        restaurants = Restaurant.objects.filter(username=username)
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

class GetEventsByUser(APIView):
    def get(self, request, username, format=None):
        events = Event.objects.filter(username=username)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

class GetTopReviewed(APIView):
    restaurant_serializer = RestaurantSerializer
    event_serializer = EventSerializer

    def get_restaurants(self):
        return Restaurant.objects.order_by('-rating')

    def get_events(self):
        return Event.objects.order_by('-start_date')

    def get(self, request, format=None):
        top_restaurants = self.restaurant_serializer(self.get_restaurants(), many = True)
        top_events = self.event_serializer(self.get_events(), many=True)
        return Response({
            "restaurants": top_restaurants.data,
            "events": top_events.data
        })

class GetLatestResults(APIView):
    restaurant_serializer = RestaurantSerializer
    event_serializer = EventSerializer
    restaurant_review_serializer = RestaurantReviewSerializer
    event_review_serializer = EventReviewSerializer

    def get(self, request, format=None):
        response_dict = {}

        restaurants = Restaurant.objects.all()
        for idx, item in enumerate(restaurants):
            reviews = RestaurantReview.objects.filter(restaurant_id = item.id)
            if reviews.exists():
                restaurant_data = self.restaurant_serializer(item).data
                reviews_data = self.restaurant_review_serializer(reviews, many=True).data
                response_dict.update({f"restaurant_entry{idx}": {
                    "restaurant": restaurant_data,
                    "reviews": reviews_data
                }})

        events = Event.objects.all()
        for idx, item in enumerate(events):
            reviews = EventReview.objects.filter(event_id = item.id)
            if reviews.exists():
                event_data = self.event_serializer(item).data
                reviews_data = self.event_review_serializer(reviews, many=True).data
                response_dict.update({f"event_entry{idx}": {
                    "event": event_data,
                    "reviews": reviews_data
                }})
        
        return Response(response_dict)

class GetRestaurantByName(APIView):
    def get(self, request, name, format=None):
        restaurant = get_object_or_404(Restaurant, name=name)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

class GetEventByName(APIView):
    def get(self, request, name, format=None):
        event = get_object_or_404(Event, name=name)
        serializer = EventSerializer(event)
        return Response(serializer.data)