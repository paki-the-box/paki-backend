'''
Module with functions for creating a shipment
'''

from rest_framework.views import APIView
from rest_framework.response import Response
from ..services.shipment import ShipmentService
from ..serializers.plainserializer import GeneralObjectSerializer
from django.http import HttpResponse, JsonResponse

class ShipmentView(APIView):
    '''
    Class for manipulation and query of shipment
    '''
    def post(self, request):
        '''
        Create a shipment
        '''
        shipmentData = request.data

        createdShipment = ShipmentService.create_shipment(shipmentData)

        serializer = GeneralObjectSerializer(createdShipment)
        serialized = serializer.data

        return JsonResponse(serialized, safe=False)
