""" Functional Test cases for Inventory Service of DSS Micro Service Layer """
import logging
import unittest
import httplib
from test.shared.rest_framework import RestAPI, RequestType, SystemType, path
from test.functional_test_suite.common.config import SYSTEM_SERVICE_URL, \
    list_system_url, list_system, initialize_logger
from test.functional_test_suite.system_service.system_service_payloads import SystemServicePayload

system_service = RestAPI(utype='customer')
invalid_system_service = RestAPI(utype='invalid')
initialize_logger(path + '/../../logs/system_service.log')


class SystemServiceTestCases(unittest.TestCase):
    """ POST: Test cases to create the systems by using POST method """

    def test_create_source_system_with_valid_details(self):
        """ Testing with valid details to create a source system """
        system_name = "TDCLOUD15TD12"

        # Create source system with valid details
        create_system_response = system_service.request(
            RequestType.POST, SYSTEM_SERVICE_URL,
            payload=SystemServicePayload().system_creation_payload())
        create_system_response_dict = create_system_response.json()
        logging.info('test_create_source_system_with_valid_details')
        logging.info('Url is %s', SYSTEM_SERVICE_URL)
        logging.info('Request is %s',
                     SystemServicePayload().system_creation_payload())
        logging.info('Response is %s', create_system_response.text)
        self.assertEquals(
            create_system_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' % (
                create_system_response.status_code,
                httplib.responses[create_system_response.status_code]))
        self.assertEquals(
            system_name, create_system_response_dict['system_name'],
            msg='Expected system name  %s and got %s' %
                (system_name, create_system_response_dict['system_name']))
        logging.info('test case executed successfully')

    def test_create_system_with_invalid_token(self):
        """ Testing with invalid token to create system """

        expected_message = "Unauthorized"

        # Create source system without system type
        create_system_response = invalid_system_service.request(
            RequestType.POST, SYSTEM_SERVICE_URL,
            payload=SystemServicePayload().system_creation_payload(details=''))
        create_system_response_dict = create_system_response.json()
        logging.info('test_create_system_with_invalid_token')
        logging.info('Url is %s', SYSTEM_SERVICE_URL)
        logging.info('Request is %s',
                     SystemServicePayload().system_creation_payload(details=''))
        logging.info('Response is %s', create_system_response.text)
        self.assertEquals(
            create_system_response.status_code, 401,
            msg='Expected 401 and got %s (%s)' %
                (create_system_response.status_code,
                 httplib.responses[create_system_response.status_code]))
        self.assertEquals(
            expected_message, create_system_response_dict['message'],
            msg=" Expecting message \"%s\" and got \"%s\" " %
                (expected_message, create_system_response_dict['message']))
        logging.info('test case executed successfully')

    def test_create_system_without_system_name(self):
        """ Test to verify blank system name parameter from payload """

        expected_message = 'System Name is not provided'

        # Create source system without system name
        create_system_response = system_service.request(
            RequestType.POST, SYSTEM_SERVICE_URL,
            payload=SystemServicePayload().system_creation_payload(
                system_name=""))
        create_system_response_dict = create_system_response.json()
        logging.info('test_create_system_without_system_name')
        logging.info('Url is %s', SYSTEM_SERVICE_URL)
        logging.info('Request is %s',
                     SystemServicePayload().system_creation_payload(
                         system_name=""))
        logging.info('Response is %s', create_system_response.text)
        self.assertEquals(
            create_system_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (create_system_response.status_code,
                 httplib.responses[create_system_response.status_code]))
        self.assertEquals(
            expected_message, create_system_response_dict['message'],
            msg='Expected message %s and got %s' %
                (expected_message, create_system_response_dict['message']))
        logging.info('test case executed successfully')

    def test_create_system_without_system_type(self):
        """ Test to verify system_type parameter passed as blank in payload """

        expected_message = 'System Type is not provided'

        # Create source system without system type
        create_system_response = system_service.request(
            RequestType.POST, SYSTEM_SERVICE_URL,
            payload=SystemServicePayload().system_creation_payload(
                system_type=""))
        create_system_response_dict = create_system_response.json()
        logging.info('test_create_system_without_system_type')
        logging.info('Url is %s', SYSTEM_SERVICE_URL)
        logging.info('Request is %s',
                     SystemServicePayload().system_creation_payload(
                         system_type=""))
        logging.info('Response is %s', create_system_response.text)
        self.assertEquals(
            create_system_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (create_system_response.status_code,
                 httplib.responses[create_system_response.status_code]))
        self.assertEquals(
            expected_message, create_system_response_dict['message'],
            msg='Expected message %s and got %s' %
                (expected_message, create_system_response_dict['message']))
        logging.info('test case executed successfully')

    def test_create_system_without_details(self):
        """ Test to verify details parameter passed as blank in payload """

        expected_message = 'System Details is not provided'

        # Create source system without system type
        create_system_response = system_service.request(
            RequestType.POST, SYSTEM_SERVICE_URL,
            payload=SystemServicePayload().system_creation_payload(details=''))
        create_system_response_dict = create_system_response.json()
        logging.info('test_create_system_without_details')
        logging.info('Url is %s', SYSTEM_SERVICE_URL)
        logging.info('Request is %s',
                     SystemServicePayload().system_creation_payload(details=''))
        logging.info('Response is %s', create_system_response.text)
        self.assertEquals(
            create_system_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (create_system_response.status_code,
                 httplib.responses[create_system_response.status_code]))
        self.assertEquals(
            expected_message, create_system_response_dict['message'],
            msg=" Expecting message \"%s\" and got \"%s\" " %
                (expected_message, create_system_response_dict['message']))
        logging.info('test case executed successfully')

    """ GET: Test cases to get the list of systems """

    def test_list_system_for_source_type(self):
        """ Testing with the given type as source to
        get list of source systems """

        # Get the source system lists
        system_list_response = system_service.request(
            RequestType.GET,
            list_system_url(list_system, SystemType.source))
        system_list_response_dict = system_list_response.json()
        logging.info('test_list_system_for_source_type')
        logging.info('Url is %s', list_system_url(
            list_system, SystemType.source))
        logging.info('Response is %s', system_list_response.text)
        self.assertEquals(
            system_list_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' %
                (system_list_response.status_code,
                 httplib.responses[system_list_response.status_code]))
        self.assertIn(
            "systems", system_list_response_dict.keys(),
            msg="Expected %s in %s" % (
                "systems", system_list_response_dict.keys()))
        logging.info('test case executed successfully')

    def test_list_system_for_target_type(self):
        """ Testing with the given type as target to
        get list of source systems  """

        # Get the target systems list
        system_list_response = system_service.request(
            RequestType.GET,
            list_system_url(list_system, SystemType.target))
        system_list_response_dict = system_list_response.json()
        logging.info('test_list_system_for_target_type')
        logging.info('Url is %s', list_system_url(
            list_system, SystemType.target))
        logging.info('Response is %s', system_list_response.text)
        self.assertEquals(
            system_list_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' %
                (system_list_response.status_code,
                 httplib.responses[system_list_response.status_code]))
        self.assertIn(
            "systems", system_list_response_dict.keys(),
            msg="Expected %s in %s" % (
                "systems", system_list_response_dict.keys()))
        logging.info('test case executed successfully')

    def test_list_systems_with_invalid_token(self):
        """ Testing without type of system to
            get list of source system """

        expected_message = "Unauthorized"

        # Get system lists without type of the system
        system_list_response = invalid_system_service.request(
            RequestType.GET, SYSTEM_SERVICE_URL)
        system_list_response_dict = system_list_response.json()
        logging.info('test_list_systems_with_invalid_token')
        logging.info('Url is %s', SYSTEM_SERVICE_URL)
        logging.info('Response is %s', system_list_response.text)
        self.assertEquals(
            system_list_response.status_code, 401,
            msg='Expected 401 and got %s (%s)' %
                (system_list_response.status_code,
                 httplib.responses[system_list_response.status_code]))
        self.assertEquals(
            expected_message, system_list_response_dict['message'],
            msg="Expected message is %s and got is %s" %
                (expected_message, system_list_response_dict['message']))
        logging.info('test case executed successfully')

    def test_list_systems_without_system_type(self):
        """ Testing without type of system to
        get list of source system """

        expected_message = 'type should be provided'

        # Get system lists without type of the system
        system_list_response = system_service.request(
            RequestType.GET, SYSTEM_SERVICE_URL)
        system_list_response_dict = system_list_response.json()
        logging.info('test_list_systems_without_system_type')
        logging.info('Url is %s', SYSTEM_SERVICE_URL)
        logging.info('Response is %s', system_list_response.text)
        self.assertEquals(
            system_list_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (system_list_response.status_code,
                 httplib.responses[system_list_response.status_code]))
        self.assertEquals(
            expected_message, system_list_response_dict['message'],
            msg="Expected message is %s and got is %s" %
                (expected_message, system_list_response_dict['message']))
        logging.info('test case executed successfully')
