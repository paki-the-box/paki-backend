'''
Module with services for shipments
'''

from ..transferobjects.shipment import CreateShipmentData

class ShipmentService:

    @staticmethod
    def create_shipment(shipment_data: CreateShipmentData):
        '''
        Create a shipment in the system
        * Validate inputs and availabilities
        * Create shipment in the Box system
        * Return the shipment information to the user
        '''
        
        return None