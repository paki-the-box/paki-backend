from django.test import TestCase

# Create your tests here.
from .services.apiclient import BoxApiClientService


class DBApiTests(TestCase):

    def setUp(self):
        print('Setup this')

    def test_get_locker_results(self):
        results = BoxApiClientService.find_locker_from_api(55.55, 10, 500000000)
        for locker in results:
            location_id = locker.location_id
            # services = BoxApiClientService.find_locker_services_from_api(location_id=location_id)
            print(locker)
            # print(services)
        #print(123)