from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class RestaurantList(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request, format=None):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)