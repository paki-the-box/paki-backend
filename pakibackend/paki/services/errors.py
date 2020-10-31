'''
Module with errors
'''

class NotFoundException(Exception):
    '''
    Exception when an object is not found
    '''
    pass

class InvalidStatusException(Exception):
    '''
    Exception when the shipment is not in the correct state
    '''
    pass