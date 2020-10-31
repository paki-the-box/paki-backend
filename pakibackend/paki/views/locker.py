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
        locations = LockerLocationService.get_all_lockers()

        serializer = GeneralObjectSerializer(locations, many=True)
        serialized = serializer.data

        return JsonResponse(serialized, safe=False)

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
