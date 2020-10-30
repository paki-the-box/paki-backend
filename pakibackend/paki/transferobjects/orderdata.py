'''
Module for defintion of order related objects
'''


class ShippedItemPhysicalProperties:
    '''
    Properties of Shipped Item
    '''
    def __init__(self):
        '''
        Initializer
        '''
        # using SI units
        self.weight: float = 0.0
        self.length: float = 0.0
        self.height: float = 0.0
        self.depth: float = 0.0


class ShippedItem:
    '''
    Properties of Shipped Item
    '''
    def __init__(self):
        '''
        Initializer
        '''
        # packaged or unpackaged item
        self.packaged: str = 'PACKAGED'
        # Barrierefrei
        self.accessible: bool = False
        # valid chars "a-zA-Z0-9.-_#/"
        self.labelId: str = ''
        # minum age to receive item
        self.requiredAge: int = 0

        self.physicalProperties: ShippedItemPhysicalProperties = None


