from .views.locker import LockerLocationsView, LockerFindView
from .views.shipment import ShipmentView
from django.urls import path
from .views import user

urlpatterns = [
    path('locker/locations', LockerLocationsView.as_view(), name='locker-locations'),
    path('locker/find/lat/<str:latitude>/long/<str:longitude>/', LockerFindView.as_view() , name='locker-find'),
    path('shipment', ShipmentView.as_view(), name='shipment-create'),
    path('shipment/<str:id>/', ShipmentView.as_view(), name='shipment-get')
    path('user/add', user.UserAddView.as_view(), name='user-add'),
    path('user/get/<str:email>', user.UserGetView.as_view(), name='user-get')
]