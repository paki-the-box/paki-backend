'''
Module providing access to the Box API
'''

import openapi_client
import requests

from openapi_client.rest import ApiException
from uuid import uuid4

from ..transferobjects.lockerdata import LockerTransferObject

class BoxApiClientService:
    '''
    Class encapsulating access to the Box API
    '''

    TOKEN_ENDPOINT = "https://auth.demo.box.deutschebahn.com/auth/realms/demo-box/protocol/openid-connect/token"
    CLIENT_ID = "d955dfb0-2097-468e-a3d7-116fe2870f3f"
    CLIENT_SECRET = "9dd8c4c5-dee9-469e-81d9-1433377f8fa0"

    _api_token = None

    # Configure OAuth2 access token for authorization: DEMO_Environment
    configuration = openapi_client.Configuration(
        host="https://api.demo.box.deutschebahn.com/v1"
    )

    @staticmethod
    def _get_access_token(token_endpoint, client_id, client_secret):
        """
        Get OAUTH client_credentials flow token
        :param token_endpoint:
        :param client_id:
        :param client_secret:
        :return:
        """
        r = requests.post(token_endpoint,
                        data=f'grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}',
                        headers={"Content-Type": "application/x-www-form-urlencoded"})
        if r.status_code != 200:
            raise Exception("Unable to get token!")
        
        return r.json().get("access_token")

    @staticmethod
    def get_locations_from_api():
        if BoxApiClientService._api_token is None:
            BoxApiClientService._api_token = BoxApiClientService._get_access_token(BoxApiClientService.TOKEN_ENDPOINT, BoxApiClientService.CLIENT_ID, BoxApiClientService.CLIENT_SECRET)
            BoxApiClientService.configuration.access_token = BoxApiClientService._api_token

        with openapi_client.ApiClient(BoxApiClientService.configuration) as api_client:
            api_instance = openapi_client.BoxAPIApi(api_client)
            locations = api_instance.get_all_locker_locations()

            mapped_results = [BoxApiClientService.map_location_results(result) for result in locations.results]

            return mapped_results

    @staticmethod
    def find_locker_from_api(latitude, longitude, radius):
        if BoxApiClientService._api_token is None:
            BoxApiClientService._api_token = BoxApiClientService._get_access_token(BoxApiClientService.TOKEN_ENDPOINT, BoxApiClientService.CLIENT_ID, BoxApiClientService.CLIENT_SECRET)
            BoxApiClientService.configuration.access_token = BoxApiClientService._api_token

        with openapi_client.ApiClient(BoxApiClientService.configuration) as api_client:
            api_instance = openapi_client.BoxAPIApi(api_client)
            locations = api_instance.get_locker_locations_nearby_geoposition(latitude, longitude, radius=radius)

            mapped_results = [BoxApiClientService.map_location_results(result) for result in locations]

            return mapped_results
    
    @staticmethod
    def map_location_results(result):
        '''
        Map from API output to our models
        '''
        lockerObject = LockerTransferObject()
        lockerObject.location_id = result.location_id

        return lockerObject
