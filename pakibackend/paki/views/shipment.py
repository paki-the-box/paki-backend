'''
Module with functions for creating a shipment
'''

from rest_framework.views import APIView
from rest_framework.response import Response
from ..services.shipment import ShipmentService
from ..serializers.plainserializer import GeneralObjectSerializer
from django.http import HttpResponse, JsonResponse
from ..services.errors import InvalidStatusException, NotFoundException

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

    def get(self, request, *args, **kwargs):
        '''
        Get info about a shipment
        '''
        try:
            shipment_id = kwargs['id']
        except KeyError as keyError:
            return HttpResponse(status=400)

        try:
            shipment = ShipmentService.get_shipment(shipment_id)
        except NotFoundException as notFound:
            return HttpResponse(status=404)

        serializer = GeneralObjectSerializer(shipment)
        serialized = serializer.data

        return JsonResponse(serialized)

class CollectionCodeView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        Get the collection code for a shipment
        '''
        try:
            shipment_id = kwargs['id']
        except KeyError as keyError:
            return HttpResponse(status=400)

        try:
            collection_data = ShipmentService.get_collection(shipment_id)
        except NotFoundException as notFoundError:
            return HttpResponse(status=404)
        except InvalidStatusException as invalidError:
            return HttpResponse(status=400)

        serializer = GeneralObjectSerializer(collection_data)
        serialized = serializer.data

        return JsonResponse(serialized)

