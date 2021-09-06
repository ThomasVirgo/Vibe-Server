from . import views
from django.urls import path


urlpatterns = [
    path('', views.index),
    path('restaurant-search/<str:query>/', views.get_restaurants)
]