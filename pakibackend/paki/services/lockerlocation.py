'''
Module for locker location service
'''
import random
import uuid

from ..transferobjects.lockerdata import LockerTransferObject, GpsCoordinates, LockerAddress, \
    LockerCompartmentSpecification, LockerCompartmentInventory


class LockerLocationService:

    @staticmethod
    def get_locker_at_location(latitude: float, longitude: float, radius: float):
        '''
        Get the lockers at a certain location
        '''

        locker_list = []

        for lockers in range(1, 10):
            test = LockerTransferObject()
            test.location_id = uuid.uuid4().hex
            test.description = "SuperBox {}".format(lockers)
            coordinates = GpsCoordinates()

            coordinates.latitude = latitude + ((random.random()-0.5)/20)
            coordinates.longitude = longitude + ((random.random()-0.5)/20)
            coordinates.altitude = 150.0
            coordinates.accuracy = 7.0
            test.geolocation = coordinates
            locker_address = LockerAddress()
            locker_address.streetAndNumber = "SuperStraße {}".format(lockers)
            locker_address.zipCode = 41120+lockers
            locker_address.city = "MegaStadt{}".format(lockers)
            locker_address.countryCode = 'DE'
            locker_address.state = 'NRW'
            test.address = locker_address
            invent_list = []
            for comp in range (1,5):
                inventory = LockerCompartmentInventory()
                spec = LockerCompartmentSpecification()
                spec.max_weigth = 1000*comp
                if comp == 1:
                    spec.size_type = 'XS'
                    spec.length = 50
                    spec.height = 50
                    spec.depth = 50
                if comp == 2:
                    spec.size_type = 'S'
                    spec.length = 150
                    spec.height = 150
                    spec.depth = 150
                if comp == 3:
                    spec.size_type = 'M'
                    spec.length = 250
                    spec.height = 250
                    spec.depth = 250
                if comp == 4:
                    spec.size_type = 'L'
                    spec.length = 350
                    spec.height = 350
                    spec.depth = 350
                if comp == 5:
                    spec.size_type = 'XL'
                    spec.length = 450
                    spec.height = 450
                    spec.depth = 450
                inventory.compartment_specification = spec
                inventory.quantityAvailable = 3 + comp
                inventory.quantityTotal = 1 + comp
                invent_list.append(inventory)
            test.compartments = invent_list
            locker_list.append(test)

        return locker_list