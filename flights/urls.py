from django.urls import path
from .views import FlightDetailView, FlightListView

urlpatterns = [
    path('flights/', FlightListView.as_view()),
    path('flights/<int:pk>/', FlightDetailView.as_view()),
]