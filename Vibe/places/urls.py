from . import views
from django.urls import path


urlpatterns = [
    path('restaurants/', views.RestaurantList.as_view()),
    path('restaurants/<int:restaurant_id>', views.RestaurantDetail.as_view()),
    path('restaurants/reviews/<int:restaurant_id>/', views.GetRestaurantReviews.as_view()), 
    path('restaurant-reviews/', views.RestaurantReviewList.as_view()),
    path('restaurant-reviews/<int:review_id>/', views.RestaurantReviewDetail.as_view()), 
    path('events/', views.EventList.as_view()),
    path('events/<int:event_id>', views.EventDetail.as_view()),
    path('events/reviews/<int:event_id>', views.GetEventReviews.as_view()),
    path('event-reviews/', views.EventReviewList.as_view()),
    path('event-reviews/<int:review_id>/', views.EventReviewDetail.as_view()), 
]