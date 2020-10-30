from .views.locker import LockerLocationsView, LockerFindView
from .views.shipment import ShipmentView
from django.urls import path

urlpatterns = [
    path('locker/locations', LockerLocationsView.as_view(), name='locker-locations'),
    path('locker/find/lat/<str:latitude>/long/<str:longitude>/', LockerFindView.as_view() , name='locker-find'),
    path('shipment', ShipmentView.as_view(), name='shipment-create'),
    path('shipment/<str:id>/', ShipmentView.as_view(), name='shipment-get')
]