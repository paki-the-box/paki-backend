'''
Module for locker location service
'''

from ..transferobjects.lockerdata import LockerTransferObject
from .apiclient import BoxApiClientService

class LockerLocationService:

    @staticmethod
    def get_all_lockers():
        '''
        Get all lockers
        '''
        return BoxApiClientService.get_locations_from_api()

    @staticmethod
    def get_locker_at_location(latitude: float, longitude: float, radius: float):
        '''
        Get the lockers at a certain location
        '''
        return BoxApiClientService.find_locker_from_api(latitude, longitude, radius) 