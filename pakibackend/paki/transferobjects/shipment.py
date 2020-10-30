'''
Module with data model for the shipment 
'''

from .orderdata import ShippedItem

class CreateShipmentData:
    '''
    Class for definition of shipments
    '''
    def __init__(self):
        self.sending_user_id : int = 0
        self.receiving_user_id : int = 0
        self.shipped_item : ShippedItem = None
        self.starting_locker_id : str = None
        self.destination_locker_id : str = None

class Shipment:
    '''
    Class for an existing shipment
    '''
    def __init__(self):
        '''
        Initializer for the class
        '''
        self.shipment_id: str = None
        self.sending_user_id: int = 0
        self.receiving_user_is: int = 0
        self.shipped_item: ShippedItem = None
        self.starting_locker_id: str = None
        self.destination_locker_id: str = None
        self.shipment_status: str = None
