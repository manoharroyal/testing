""" Functional Test cases for Inventory Service of DSS Micro Service Layer """
import logging
import unittest
import httplib
from test.shared.rest_framework import RestAPI, RequestType, SystemType
from test.functional_test_suite.common.config import SYSTEM_SERVICE_URL, \
    SYSTEM_SERVICE, list_system_url, source_system_url, target_system_url, \
    list_system, target_system, source_system, SOURCE_SYSTEM_ID
from test.functional_test_suite.common.payloads import SystemServicePayload

system_service = RestAPI(utype='customer')
invalid_system_service = RestAPI(utype='invalid')


class SystemServiceTestCases(unittest.TestCase):
    """ POST: Test cases to create the systems by using POST method """

    def test_create_source_system(self):
        """ Testing with valid details to create a source system """
        system_name = "TDCLOUD15TD12"

        # Create source system with valid details
        create_system_response = system_service.request(
            RequestType.POST, SYSTEM_SERVICE_URL,
            payload=SystemServicePayload().system_creation_payload())
        create_system_response_dict = create_system_response.json()
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

    def test_create_system_with_missing_system_name_from_payload(self):
        """ Test to verify missing system name parameter from payload """

        expected_message = 'System Name is not provided'

        # Create source system with missing system from payload
        create_system_response = system_service.request(
            RequestType.POST, SYSTEM_SERVICE_URL,
            payload=SystemServicePayload().system_deletion_payload(
                "system_name"))
        create_system_response_dict = create_system_response.json()
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

    def test_create_system_with__missing_system_type_from_payload(self):
        """ Test to verify missing system type parameter from payload """

        expected_message = 'System Type is not provided'

        # Create source system with missing system type from payload
        create_system_response = system_service.request(
            RequestType.POST, SYSTEM_SERVICE_URL,
            payload=SystemServicePayload().system_deletion_payload(
                "system_type"))
        create_system_response_dict = create_system_response.json()
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

    def test_create_system_with__missing_details_from_payload(self):
        """ Test to verify missing details parameter from payload """

        expected_message = 'System Details is not provided'

        # Create source system with missing details from payload
        create_system_response = system_service.request(
            RequestType.POST, SYSTEM_SERVICE_URL,
            payload=SystemServicePayload().system_deletion_payload("details"))
        create_system_response_dict = create_system_response.json()
        logging.info('Response is %s', create_system_response.text)
        self.assertEquals(
            create_system_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (create_system_response.status_code,
                 httplib.responses[create_system_response.status_code]))
        self.assertEquals(
            expected_message, create_system_response_dict['message'],
            msg='Expected message %s and got %s' %
                (expected_message,  create_system_response_dict['message']))

    def test_create_system_without_system_name(self):
        """ Test to verify blank system name parameter from payload """

        expected_message = 'System Name is not provided'

        # Create source system without system name
        create_system_response = system_service.request(
            RequestType.POST, SYSTEM_SERVICE_URL,
            payload=SystemServicePayload().system_creation_payload(
                system_name=""))
        create_system_response_dict = create_system_response.json()
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

    def test_create_system_without_system_type(self):
        """ Test to verify system_type parameter passed as blank in payload """

        expected_message = 'System Type is not provided'

        # Create source system without system type
        create_system_response = system_service.request(
            RequestType.POST, SYSTEM_SERVICE_URL,
            payload=SystemServicePayload().system_creation_payload(
                system_type=""))
        create_system_response_dict = create_system_response.json()
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

    def test_create_system_without_details(self):
        """ Test to verify details parameter passed as blank in payload """

        expected_message = 'System Details is not provided'

        # Create source system without system type
        create_system_response = system_service.request(
            RequestType.POST, SYSTEM_SERVICE_URL,
            payload=SystemServicePayload().system_creation_payload(details=''))
        create_system_response_dict = create_system_response.json()
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

    """ GET: Test cases to get the list of systems """

    def test_list_system_for_source_type(self):
        """ Testing with the given type as source to
        get list of source systems """

        # Get the source system lists
        system_list_response = system_service.request(
            RequestType.GET,
            list_system_url(list_system, SystemType.source))
        logging.info('Response is %s', system_list_response.text)
        self.assertEquals(
            system_list_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' %
                (system_list_response.status_code,
                 httplib.responses[system_list_response.status_code]))

    def test_list_system_for_target_type(self):
        """ Testing with the given type as target to
        get list of source systems  """

        # Get the target systems list
        system_list_response = system_service.request(
            RequestType.GET,
            list_system_url(list_system, SystemType.target))
        logging.info('Response is %s', system_list_response.text)
        self.assertEquals(
            system_list_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' %
                (system_list_response.status_code,
                 httplib.responses[system_list_response.status_code]))

    def test_list_systems_with_missing_type_url(self):
        """ Testing without type of system to
        get list of source system """

        expected_message = 'type should be provided'

        # Get system lists without type of the system
        system_list_response = system_service.request(
            RequestType.GET, SYSTEM_SERVICE_URL)
        response_dict = system_list_response.json()
        logging.info('Response is %s', system_list_response.text)
        self.assertEquals(
            system_list_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (system_list_response.status_code,
                 httplib.responses[system_list_response.status_code]))
        self.assertEquals(
            expected_message, response_dict['message'],
            msg="Expected message is %s and got is %s" %
                (expected_message, response_dict['message']))

    def test_list_systems_with_misspelled_in_url(self):
        """ Testing with invalid url to get the list details of system """

        # Get the system lists with invalid url
        system_list_response = system_service.request(
            RequestType.GET, SYSTEM_SERVICE_URL + '/?type1')
        system_list_response_dict = system_list_response.json()
        logging.info('Response is %s', system_list_response.text)
        self.assertEquals(
            system_list_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (system_list_response.status_code,
                 httplib.responses[system_list_response.status_code]))
        self.assertIn(
            'message', system_list_response_dict.keys(),
            msg="Expected %s equals %s" %
                ('message', system_list_response_dict.keys()))

    """ GET: Test cases to check with the parameters to get the
    details of particular system by passing system id """

    def test_system_details_with_valid_source_system(self):
        """ Testing with valid details to get the source system details """

        # Get the system details with valid source system id
        system_details_response = system_service.request(
            RequestType.GET,
            source_system_url(source_system, SOURCE_SYSTEM_ID))
        source_system_details = system_details_response.json()
        logging.info('Response is %s', system_details_response.text)
        self.assertEquals(
            system_details_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' %
                (system_details_response.status_code,
                 httplib.responses[system_details_response.status_code]))
        self.assertIn(
            'details', source_system_details.keys(),
            msg="Expected %s in %s" % ('details', source_system_details.keys()))

    def test_system_details_with_valid_target_system(self):
        """ Testing with valid details to get the target system details """

        # Get the system details with valid target system id
        system_details_response = system_service.request(
            RequestType.GET, target_system_url(target_system, 'KAGAWS3'))
        target_system_details = system_details_response.json()
        logging.info('Response is %s', system_details_response.text)
        self.assertEquals(
            system_details_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' %
                (system_details_response.status_code,
                 httplib.responses[system_details_response.status_code]))
        self.assertIn(
            'result', target_system_details.keys(),
            msg="Expected %s in %s" % ('result', target_system_details.keys()))

    def test_system_details_without_system_id(self):
        """ Testing without system id to get the source system details  """

        # Get the system details without system id
        system_details_response = system_service.request(
            RequestType.GET, source_system_url(source_system, ''))
        system_details_response_dict = system_details_response.json()
        logging.info('Response is %s', system_details_response.text)
        self.assertEquals(
            system_details_response.status_code, 403,
            msg='Expected 403 and got %s (%s)' %
                (system_details_response.status_code,
                 httplib.responses[system_details_response.status_code]))
        self.assertIn(
            'message', system_details_response_dict.keys(),
            msg="Expected %s in %s" %
                ('message', system_details_response_dict.keys()))

    def test_system_details_with_invalid_system_id(self):
        """ Testing with invalid system id to get the source system details """

        expected_message = "Resource with id 123 does not exists"

        # Get the system details without system id
        system_details_response = system_service.request(
            RequestType.GET,
            source_system_url(source_system, '123'))
        system_details_response_dict = system_details_response.json()
        logging.info('Response is %s', system_details_response.text)
        self.assertEquals(
            system_details_response.status_code, 404,
            msg='Expected 404 and got %s (%s)' %
                (system_details_response.status_code,
                 httplib.responses[system_details_response.status_code]))
        self.assertEquals(
            expected_message, system_details_response_dict['message'],
            msg="Expected message is %s and got is %s" %
                (expected_message, system_details_response_dict['message']))

    """ GET: Test cases to get the system details of customer """

    def test_get_system_with_valid_customer(self):
        """ Testing with the valid url to get the system details of customer """

        # Get the list systems of customer
        customer_systems_response = system_service.request(
            RequestType.GET, SYSTEM_SERVICE + '/customer')
        customer_systems_response_dict = customer_systems_response.json()
        logging.info('Response is %s', customer_systems_response.text)
        self.assertEquals(
            customer_systems_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' %
                (customer_systems_response.status_code,
                 httplib.responses[customer_systems_response.status_code]))
        self.assertIn('details', customer_systems_response_dict.keys(),
                      msg="Expecting %s in %s" %
                          ('details', customer_systems_response_dict.keys()))

    def test_get_systems_customer_with_invalid_token(self):
        """ Testing with the invalid token to get customer system details """

        expected_message = 'exceptions while validating token'

        # Get the list systems of customer with invalid token
        customer_systems_response = invalid_system_service.request(
            RequestType.GET, SYSTEM_SERVICE + '/customer')
        customer_systems_response_dict = customer_systems_response.json()
        logging.info('Response is %s', customer_systems_response.text)
        self.assertEquals(
            customer_systems_response.status_code, 401,
            msg='Expected 401 and got %s (%s)' %
                (customer_systems_response.status_code,
                 httplib.responses[customer_systems_response.status_code]))
        self.assertIn(
            expected_message, customer_systems_response_dict['message'],
            msg="Expected message is %s in %s" %
                (expected_message, customer_systems_response_dict['message']))

    def test_get_systems_customer_with_invalid_url(self):
        """ Testing with invalid url to get the details of customer """

        # Get the list systems of customer with invalid url
        customer_systems_response = system_service.request(
            RequestType.GET, SYSTEM_SERVICE_URL + '/customer1')
        customer_systems_response_dict = customer_systems_response.json()
        logging.info('Response is %s', customer_systems_response.text)
        self.assertEquals(
            customer_systems_response.status_code, 403,
            msg='Expected 400 and got %s (%s)' %
                (customer_systems_response.status_code,
                 httplib.responses[customer_systems_response.status_code]))
        self.assertIn(
            'message', customer_systems_response_dict.keys(),
            msg="Expecting %s in %s" %
                ('message', customer_systems_response_dict.keys()))
