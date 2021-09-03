from . import views
from django.urls import path


urlpatterns = [
    path('restaurants/', views.RestaurantList.as_view()),
    path('restaurants/<int:restaurant_id>', views.RestaurantDetail.as_view()),
]