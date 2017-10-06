""" Functional Test cases for Inventory Service of DSS Micro Service Layer """
import unittest
from common.rest_framework import RestAPIHeader
from common.helper_function import RequestType
from common.config import SYSTEM_SERVICE_URL, SYSTEM_API_URL, list_system_url, \
    source_system_url, target_system_url, list_system, target_system, \
    source_system
from common.payloads import SystemServicePayload
system_service = RestAPIHeader()
system_service_invalid_token = RestAPIHeader(utype='un user')


class SystemServicePostTestCases(unittest.TestCase):
    """ Test cases to create the systems by using POST method """

    def test_create_source_system(self):
        """ Testing with valid details to create a source system """
        out = system_service.request(RequestType.POST, SYSTEM_SERVICE_URL,
                                     payload=SystemServicePayload().
                                     system_creation_payload())
        out_dict = out.json()
        self.assertEquals(out.status_code, 200)
        self.assertEquals(out_dict['system_name'], "TDCLOUD15TD12")

    def test_missing_system_name_from_payload(self):
        """ Test to verify missing system name parameter from payload """
        out = system_service.request(RequestType.POST, SYSTEM_SERVICE_URL,
                                     payload=SystemServicePayload().
                                     system_deletion_payload("system_name"))
        out_dict = out.json()
        message = 'System Name is not provided'
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], message)

    def test_missing_system_type_from_payload(self):
        """ Test to verify missing system type parameter from payload """
        out = system_service.request(RequestType.POST, SYSTEM_SERVICE_URL,
                                     payload=SystemServicePayload().
                                     system_deletion_payload("system_type"))
        out_dict = out.json()
        message = 'System Type is not provided'
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], message)

    def test_missing_details_from_payload(self):
        """ Test to verify missing details parameter from payload """
        out = system_service.request(RequestType.POST, SYSTEM_SERVICE_URL,
                                     payload=SystemServicePayload().
                                     system_deletion_payload("details"))
        out_dict = out.json()
        message = 'System Details is not provided'
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], message)

    def test_without_system_name(self):
        """ Test to verify blank system name parameter from payload """
        out = system_service.request(RequestType.POST, SYSTEM_SERVICE_URL,
                                     payload=SystemServicePayload().
                                     system_creation_payload(system_name=""))
        out_dict = out.json()
        message = 'System Name is not provided'
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], message)

    def test_withoutsystem_type(self):
        """ Test to verify system_type parameter passed as blank in payload """
        out = system_service.request(RequestType.POST, SYSTEM_SERVICE_URL,
                                     payload=SystemServicePayload().
                                     system_creation_payload(system_type=""))
        out_dict = out.json()
        message = 'System Type is not provided'
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], message)

    def test_without_details(self):
        """ Test to verify details parameter passed as blank in payload """
        out = system_service.request(RequestType.POST, SYSTEM_SERVICE_URL,
                                     payload=SystemServicePayload().
                                     system_creation_payload(details=''))
        out_dict = out.json()
        message = 'System Details is not provided'
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], message)


class SystemServiceGetTestCases(unittest.TestCase):
    """ Test cases to get the list of systems """

    def test_list_system_for_source_type(self):
        """ Testing with the given type as source to
        get list of source systems """
        out = system_service.request(RequestType.GET,
                                     list_system_url(list_system, 'source'))
        self.assertEquals(out.status_code, 200)

    def test_list_system_for_target_type(self):
        """ Testing with the given type as target to
        get list of source systems  """
        out = system_service.request(RequestType.GET,
                                     list_system_url(list_system, 'target'))
        self.assertEquals(out.status_code, 200)

    def test_missing_type_error_message(self):
        """ Testing without type of system to
        get list of source system """
        out = system_service.request(RequestType.GET, SYSTEM_SERVICE_URL)
        out_dict = out.json()
        message = 'type should be provided'
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], message)

    def test_type_misspelled_in_url(self):
        """ Testing with invalid url to get the list details of system """
        out = system_service.request(RequestType.GET,
                                     SYSTEM_SERVICE_URL + '/?type')
        out_dict = out.json()
        message = 'type should be provided'
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], message)


class SystemServiceGetSystemDetailsTestCases(unittest.TestCase):
    """ Test cases to check with the parameters to get the
    details of particular system by passing system id """

    def test_list_details_for_given_source_system(self):
        """ Testing with valid details to get the source system details """
        out = system_service.request(RequestType.GET,
                                     source_system_url
                                     (source_system,
                                      'e0cd3fd3-8281-4fde-a47b-cdbb2b7ee2fc'))
        self.assertEquals(out.status_code, 200)

    def test_list_details_for_given_target_system(self):
        """ Testing with valid details to get the target system details """
        out = system_service.request(RequestType.GET,
                                     target_system_url(target_system,
                                                       'KAGAWS3'))
        self.assertEquals(out.status_code, 200)

    def test_missing_system_id_error_message(self):
        """ Testing without system id to get the source system details  """
        out = system_service.request(RequestType.GET,
                                     source_system_url(source_system, ''))
        self.assertEquals(out.status_code, 403)

    def test_invalid_system_id_error_message(self):
        """ Testing with invalid system id to get the source system details """
        out = system_service.request(RequestType.GET,
                                     source_system_url(source_system, '123'))
        out_dict = out.json()
        message = "Resource with id 123 does not exists"
        self.assertEquals(out.status_code, 404)
        self.assertEquals(out_dict['message'], message)


class SystemServiceGetCustomerName(unittest.TestCase):
    """ Test cases to get the system details of customer """

    def test_get_customer_name(self):
        """ Testing with the valid url to get the system details of customer """
        out = system_service.request(RequestType.GET,
                                     SYSTEM_API_URL + '/customer')
        out_dict = out.json()
        self.assertEquals(out.status_code, 200)
        self.assertIn('details', out_dict.keys())

    def test_get_customer_name_for_invalid_token(self):
        """ Testing with the invalid token to get customer system details """
        out = system_service_invalid_token.request(RequestType.GET,
                                                   SYSTEM_API_URL + '/customer')
        out_dict = out.json()
        message = 'exceptions while validating token'
        self.assertEquals(out.status_code, 401)
        self.assertIn(message, out_dict['message'])

    def test_get_customer_name_for_invalid_url(self):
        """ Testing with invalid url to get the details of customer """
        out = system_service.request(RequestType.GET,
                                     SYSTEM_API_URL + '/customer1')
        out_dict = out.json()
        self.assertEquals(out.status_code, 403)
        self.assertIn('message', out_dict.keys())


if __name__ == '__main__':
    unittest.main()
