'''
Module with data model for the shipment 
'''

from .orderdata import ShippedItem

class CreateShipmentData:
    def __init__(self):
        self.sending_user_id : int = 0
        self.receiving_user_id : int = 0
        self.shipped_item : ShippedItem = None
        self.starting_locker_id : str = None
        self.destination_locker_id : str = None