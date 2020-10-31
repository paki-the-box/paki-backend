'''
Module with services for shipments
'''

from ..transferobjects.shipment import CreateShipmentData, Shipment, CollectionCodeData
from ..transferobjects.orderdata import ShippedItem, ShippedItemPhysicalProperties
from .errors import NotFoundException
from .apiclient import BoxApiClientService
from ..models import HandoverTransaction

class ShipmentService:

    @staticmethod
    def shipment_from_transaction(transaction: HandoverTransaction):
        '''
        Get the shipment data from the transaction information
        '''
        shipment_data = CreateShipmentData()
        shipment_data.starting_locker_id = transaction.box_id
        
        shipment_data.shipped_item = ShippedItem()
        shipment_data.shipped_item.physicalPropeties = ShippedItemPhysicalProperties()
        
        return shipment_data

    @staticmethod
    def create_shipment(transaction: HandoverTransaction):
        '''
        Create a shipment in the system
        * Validate inputs and availabilities
        * Create shipment in the Box system
        * Return the shipment information to the user
        '''
        #TODO: Implement this
        shipment_data = ShipmentService.shipment_from_transaction(transaction)
        response = BoxApiClientService.create_shipment(shipment_data)
        return response

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