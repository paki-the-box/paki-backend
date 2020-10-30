'''
Module for locker location service
'''

from ..transferobjects.lockerdata import LockerTransferObject

class LockerLocationService:

    @staticmethod
    def get_locker_at_location(latitude: float, longitude: float, radius: float):
        '''
        Get the lockers at a certain location
        '''
        return []