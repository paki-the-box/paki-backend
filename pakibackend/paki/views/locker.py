from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import authentication, permissions
from django.http import HttpResponse, JsonResponse

from ..serializers.plainserializer import FlatObjectSerializer
from ..transferobjects.lockerdata import LockerTransferObject
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
        
        serializer = FlatObjectSerializer(test)
        serialized = serializer.data
        return JsonResponse(serialized)