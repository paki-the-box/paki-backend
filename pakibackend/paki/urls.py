from .views.locker import LockerLocationsView 
from django.urls import path

urlpatterns = [
    path('locker/locations', LockerLocationsView.as_view(), name='locker-locations')
]