from . import views
from django.urls import path


urlpatterns = [
    path('restaurants/', views.RestaurantList.as_view()),
]