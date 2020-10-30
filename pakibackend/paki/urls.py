from .views.locker import LockerLocationsView, LockerFindView
from django.urls import path

urlpatterns = [
    path('locker/locations', LockerLocationsView.as_view(), name='locker-locations'),
    path('locker/find/lat/<str:latitude>/long/<str:longitude>/', LockerFindView.as_view() , name='locker-find')
]