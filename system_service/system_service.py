import unittest
from common.rest_framework import RestAPIHeader, RequestType
from common.config import SYSTEM_SERVICE_URL, SYSTEM_API_URL
from common.payloads import SystemServicePayload

list_system = SYSTEM_SERVICE_URL + "/?type="
source_system = SYSTEM_SERVICE_URL + "/source/"
target_system = SYSTEM_SERVICE_URL + "/target/"

system_rest_obj = RestAPIHeader()


def list_system_url(list_system, system_type):
    """ Url to get the list of systems """
    return '%s%s' % (list_system, system_type)


def source_system_url(source_system, system_id):
    """ Url to get the details of source system """
    return '%s%s' % (source_system, system_id)


def target_system_url(target_system, site_id):
    """ Url to get the details of target system"""
    return '%s%s' % (target_system, site_id)


class SystemServicePostTestCases(unittest.TestCase):
    """ Test cases to create the systems by using POST method """

    def test_create_source_system(self):
        """ Test to create a source system with the valid details """

        out = system_rest_obj.request(RequestType.POST, SYSTEM_SERVICE_URL,
                                      payload=SystemServicePayload().
                                      system_creation_payload
                                      (system_name="TDCLOUD15TD12"))
        out_dict = out.json()
        self.assertEquals(out.status_code, 200)
        self.assertEquals(out_dict['system_name'], "TDCLOUD15TD12")

    def test_create_target_system(self):
        """ Test to create a system target system with valid details """

        out = system_rest_obj.request(RequestType.POST, SYSTEM_SERVICE_URL,
                                      payload=SystemServicePayload().
                                      system_creation_payload
                                      (system_name="TDCLOUD15TD13",
                                       system_type='target'))
        out_dict = out.json()
        self.assertEquals(out.status_code, 200)
        self.assertEquals(out_dict['system_name'], 'TDCLOUD15TD13')

    def test_missing_system_name_from_payload(self):
        """ Test to verify missing system name parameter from payload """

        out = system_rest_obj.request(RequestType.POST, SYSTEM_SERVICE_URL,
                                      payload=SystemServicePayload().
                                      system_deletion_payload
                                      ("system_name"))
        out_dict = out.json()
        message = 'System Name is not provided'
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], message)

    def test_missing_system_type_from_payload(self):
        """ Test to verify missing system type parameter from payload """

        out = system_rest_obj.request(RequestType.POST, SYSTEM_SERVICE_URL,
                                      payload=SystemServicePayload().
                                      system_deletion_payload("system_type"))
        out_dict = out.json()
        message = 'System Type is not provided'
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], message)

    def test_missing_details_from_payload(self):
        """ Test to verify missing details parameter from payload """

        out = system_rest_obj.request(RequestType.POST, SYSTEM_SERVICE_URL,
                                      payload=SystemServicePayload().
                                      system_deletion_payload("details"))
        out_dict = out.json()
        message = 'System Details is not provided'
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], message)

    def test_with_blank_system_name(self):
        """ Test to verify blank system name parameter from payload """

        out = system_rest_obj.request(RequestType.POST, SYSTEM_SERVICE_URL,
                                      payload=SystemServicePayload().
                                      system_creation_payload(system_name=""))
        out_dict = out.json()
        message = 'System Name is not provided'
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], message)

    def test_with_blank_system_type(self):
        """ Test to verify system_type parameter passed as blank in payload """

        out = system_rest_obj.request(RequestType.POST, SYSTEM_SERVICE_URL,
                                      payload=SystemServicePayload().
                                      system_creation_payload(system_type=""))
        out_dict = out.json()
        message = 'System Type is not provided'
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], message)

    def test_with_blank_details(self):
        """ Test to verify details parameter passed as blank in payload """

        out = system_rest_obj.request(RequestType.POST, SYSTEM_SERVICE_URL,
                                      payload=SystemServicePayload().
                                      system_creation_payload(details=' '))
        out_dict = out.json()
        message = 'System Details is not provided'
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], message)


class SystemServiceGetTestCases(unittest.TestCase):
    def test_list_system_for_source_type(self):
        """ Test to create a system """

        out = system_rest_obj.request(RequestType.GET,
                                      list_system_url(list_system, 'source'))
        self.assertEquals(out.status_code, 200)

    def test_list_system_for_target_type(self):
        """ Test to create a system  """

        out = system_rest_obj.request(RequestType.GET,
                                      list_system_url(list_system, 'target'))
        self.assertEquals(out.status_code, 200)

    def test_missing_type_error_message(self):
        """ Test for missing type from url """

        out = system_rest_obj.request(RequestType.GET, SYSTEM_SERVICE_URL)
        out_dict = out.json()
        message = 'type should be provided'
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], message)

    def test_type_misspelled_in_url(self):
        """ Test for misspelling of type """

        out = system_rest_obj.request(RequestType.GET,
                                      SYSTEM_SERVICE_URL + '/?tpe')
        out_dict = out.json()
        message = 'type should be provided'
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], message)


#

class SystemServiceGetSystemDetailsTestCases(unittest.TestCase):
    def test_list_details_for_given_source_system(self):
        """ Test to get the details of system """

        out = system_rest_obj.request(RequestType.GET,
                                      source_system_url
                                      (source_system,
                                       'e0cd3fd3-8281-4fde-a47b-cdbb2b7ee2fc'))
        self.assertEquals(out.status_code, 200)

    def test_list_details_for_given_target_system(self):
        """ Test to get the details of system """

        out = system_rest_obj.request(RequestType.GET,
                                      target_system_url
                                      (target_system, 'KAGAWS3'))
        self.assertEquals(out.status_code, 200)

    def test_missing_system_id_error_message(self):
        """ Test for missing system id from url """

        out = system_rest_obj.request(RequestType.GET,
                                      source_system_url(source_system, ''))
        self.assertEquals(out.status_code, 403)

    def test_invalid_system_id_error_message(self):
        """ Test for invalid system id """

        out = system_rest_obj.request(RequestType.GET,
                                      source_system_url(source_system, '123'))
        out_dict = out.json()
        message = "Resource with id 123 does not exists"
        self.assertEquals(out.status_code, 404)
        self.assertEquals(out_dict['message'], message)


class SystemServiceGetCustomerName(unittest.TestCase):
    def test_get_customer_name(self):
        out = system_rest_obj.request(RequestType.GET,
                                      SYSTEM_API_URL + '/customer')
        self.assertEquals(out.status_code, 200)

    def test_get_customer_name_for_invalid_token(self):
        out = system_rest_obj.request(RequestType.GET,
                                      SYSTEM_API_URL + '/customer')
        out_dict = out.json()
        message = 'exceptions while validating token'
        self.assertEquals(out.status_code, 401)
        self.assertIn(out_dict['message'], message)


if __name__ == '__main__':
    unittest.main()
