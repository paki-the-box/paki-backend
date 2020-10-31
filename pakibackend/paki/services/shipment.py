'''
Module with services for shipments
'''

from ..transferobjects.shipment import CreateShipmentData, Shipment, CollectionCodeData
from .errors import NotFoundException


class ShipmentService:
    @staticmethod
    def create_shipment(shipment_data: CreateShipmentData):
        '''
        Create a shipment in the system
        * Validate inputs and availabilities
        * Create shipment in the Box system
        * Return the shipment information to the user
        '''
        #TODO: Implement this
        shipment_data = Shipment()
        return shipment_data

    @staticmethod
    def get_shipment(shipment_id: str):
        '''
        Get an existing shipment
        '''
        #TODO: Implement this
        shipment_data = Shipment()
        
        return shipment_data

    @staticmethod
    def get_collection(shipment_id: str):
        '''
        Get the collection code for a shipment 
        '''
        #TODO: Implement call to DB APi 
        collection_code = CollectionCodeData()

        return collection_code