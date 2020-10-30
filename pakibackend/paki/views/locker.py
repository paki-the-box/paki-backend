from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import authentication, permissions
from django.http import HttpResponse, JsonResponse

from ..serializers.plainserializer import POPOSerializer
from ..transferobjects.lockerdata import LockerTransferObject

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
        
        serializer = POPOSerializer(test)
        return JsonResponse(serializer.data)