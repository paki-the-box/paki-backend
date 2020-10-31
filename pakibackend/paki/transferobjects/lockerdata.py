'''
Module for defintion of trasnfer objects
'''

class LockerAddress:
    '''
    Address of a locker
    '''
    def __init__(self):
        '''
        Initializer
        '''
        self.streetAndNumber : str = None
        self.state : str = None
        self.zipCode: int = None
        self.city : str = None
        self.countryCode : str = None

class GpsCoordinates:
    '''
    Geo coordinates of the locker
    '''
    def __init__(self):
        '''
        Initializer
        '''
        self.latitude: float
        self.longitude: float
        self.altitude: float
        self.accuracy: float 

class LockerCompartmentSpecification:
    '''
    Specification data for a compartment
    '''
    def __init__(self):
        '''
        Initializer
        '''
        self.length : float
        self.height : float 
        self.depth : float 
        # Equivalent to description (S, M, L, XL)
        self.size_type: str
        self.max_weigth : float = 0.0

class LockerCompartmentInventory:
    '''
    Inventory of all compartments grouped by their specification
    '''
    def __init__(self):
        '''
        Initializer
        '''
        self.compartment_specification: LockerCompartmentSpecification = None
        self.quantityTotal: int = 0
        self.quantityAvailable: int = 0

class LockerContact:
    '''
    Responsible contact for a locker
    '''
    def __init__(self):
        self.phone : str = None
        self.email_address: str = None

class LockerTransferObject:
    '''
    Locker location object
    '''
    def __init__(self):
        '''
        Initializer
        '''
        self.location_id : str = None
        self.address : LockerAddress = None
        self.description : str = None
        self.geolocation : GpsCoordinates = None
        self.compartments: list[LockerCompartmentInventory] = []
        self.contact: LockerContact = LockerAddress()
        self.usable : bool = True
        self.is_public: bool = True