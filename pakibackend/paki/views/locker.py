from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import authentication, permissions
from django.http import HttpResponse, JsonResponse

from ..transferobjects.lockerdata import LockerTransferObject, GpsCoordinates
from ..serializers.plainserializer import GeneralObjectSerializer
from ..services.lockerlocation import LockerLocationService 
import json

class MyModel:
    def __init__(self):
        self.a = "a"
        self.b = "b"

class LockerLocationsView(APIView):
    '''
    API View to get the locations of the lockers
    '''
    def get(self, request, format = None):
        '''
        Get location of all possible boxes
        '''
        test = LockerTransferObject()
        test.location_id = "1234-621761-671628"
        coordinates = GpsCoordinates()
        coordinates.latitude = 32.0
        coordinates.longitude = 40.0
        coordinates.altitude = 150.0
        coordinates.accuracy = 7.0

        test.geolocation = coordinates
        
        serializer = GeneralObjectSerializer(test)
        serialized = serializer.data
        return JsonResponse(serialized)

class LockerFindView(APIView):
    '''
    View for finding lockers near a position
    '''
    def get(self, request, format = None, *args, **kwargs):
        '''
        Get data for locker from location
        ''' 
        lat = float(kwargs['latitude'])
        long = float(kwargs['longitude'])

        radius = self.request.query_params.get('radius', 50.0)

        lockers = LockerLocationService.get_locker_at_location(lat, long, radius)
        serializer = GeneralObjectSerializer(lockers)
        serialized = serializer.data

        return JsonResponse(serialized)
