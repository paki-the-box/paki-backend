from .views.locker import LockerLocationsView 
from django.urls import path
from .views import user

urlpatterns = [
    path('locker/locations', LockerLocationsView.as_view(), name='locker-locations'),
    path('user/add', user.UserAddView.as_view(), name='user-add'),
    path('user/get/<str:email>', user.UserGetView.as_view(), name='user-get')
]